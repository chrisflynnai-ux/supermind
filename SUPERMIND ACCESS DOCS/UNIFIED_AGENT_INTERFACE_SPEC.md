# UNIFIED AGENT INTERFACE (UAI) SPECIFICATION
## ULTRAMIND Agentic Architecture — Agent Abstraction Layer

**Version:** 1.0.0  
**Status:** Draft Specification  
**Doctrine:** Lean at Zero-Point, Heavy at Edges

---

## EXECUTIVE SUMMARY

The Unified Agent Interface (UAI) provides a standardized abstraction layer for integrating multiple AI agent systems (Abacus, Agent Zero, Manus, Pydantic AI, and future agents) into a single coherent orchestration framework.

**Problem:** Each agent system has different APIs, authentication, error handling, and state management patterns. Direct integration creates tight coupling and maintenance overhead.

**Solution:** A thin abstraction layer that normalizes all agent interactions through a common interface, enabling the orchestrator to route tasks without knowing implementation details.

---

## DESIGN PRINCIPLES

1. **Interface Segregation** — Agents implement only what they support
2. **Dependency Inversion** — Orchestrator depends on abstractions, not concrete agents
3. **Fail-Fast with Fallback** — Quick error detection, graceful degradation
4. **Stateless Calls, Stateful Context** — Agents are stateless; Convex holds state
5. **Observable by Default** — All operations emit structured logs

---

## CORE INTERFACES

### 1. Base Agent Interface

```python
from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class AgentCapability(str, Enum):
    """Standard capability categories"""
    BUILD = "build"           # App/code generation
    EXECUTE = "execute"       # Local command execution
    RESEARCH = "research"     # Information gathering
    VALIDATE = "validate"     # Quality assurance
    COMMUNICATE = "communicate"  # User interaction
    ANALYZE = "analyze"       # Data analysis
    DEPLOY = "deploy"         # Infrastructure operations

class AgentStatus(str, Enum):
    """Agent operational states"""
    IDLE = "idle"
    WORKING = "working"
    BLOCKED = "blocked"
    ERROR = "error"
    OFFLINE = "offline"

class TaskPriority(str, Enum):
    """Task urgency levels"""
    CRITICAL = "critical"     # Immediate, blocks everything
    HIGH = "high"             # Next in queue
    NORMAL = "normal"         # Standard processing
    LOW = "low"               # Background/async
    DEFERRED = "deferred"     # Run when idle

class TaskResult(BaseModel):
    """Standardized result from any agent"""
    success: bool
    task_id: str
    agent_id: str
    capability_used: AgentCapability
    output: Any
    artifacts: List[str] = []          # File paths, URLs created
    tokens_used: Optional[int] = None
    duration_ms: int
    error: Optional[str] = None
    error_code: Optional[str] = None
    fallback_suggested: Optional[str] = None
    insights: List[str] = []           # Learning for insights.md
    timestamp: datetime

class TaskRequest(BaseModel):
    """Standardized request to any agent"""
    task_id: str
    instruction: str
    capability: AgentCapability
    priority: TaskPriority = TaskPriority.NORMAL
    context: Dict[str, Any] = {}       # From context.md / Convex
    constraints: Dict[str, Any] = {}   # Time limits, token budgets
    fallback_agents: List[str] = []    # Try these if primary fails
    callback_url: Optional[str] = None # For async completion
    timeout_seconds: int = 300

class AgentMetadata(BaseModel):
    """Agent self-description"""
    agent_id: str
    name: str
    version: str
    capabilities: List[AgentCapability]
    max_concurrent_tasks: int
    avg_response_time_ms: int
    cost_per_1k_tokens: Optional[float]
    requires_auth: bool
    supports_async: bool
    supports_streaming: bool

class IAgent(ABC):
    """
    Unified Agent Interface
    
    All agent implementations must inherit from this class
    and implement the required methods.
    """
    
    @property
    @abstractmethod
    def metadata(self) -> AgentMetadata:
        """Return agent capabilities and configuration"""
        pass
    
    @abstractmethod
    async def execute(self, request: TaskRequest) -> TaskResult:
        """
        Execute a task synchronously.
        
        Args:
            request: Standardized task request
            
        Returns:
            TaskResult with output or error
        """
        pass
    
    @abstractmethod
    async def execute_async(self, request: TaskRequest) -> str:
        """
        Start async task execution.
        
        Args:
            request: Standardized task request
            
        Returns:
            Task ID for status polling
        """
        pass
    
    @abstractmethod
    async def get_status(self, task_id: str) -> TaskResult:
        """
        Get status of async task.
        
        Args:
            task_id: ID returned from execute_async
            
        Returns:
            Current TaskResult (may be partial if still running)
        """
        pass
    
    @abstractmethod
    async def cancel(self, task_id: str) -> bool:
        """
        Cancel a running task.
        
        Args:
            task_id: ID of task to cancel
            
        Returns:
            True if cancelled, False if already complete or not found
        """
        pass
    
    @abstractmethod
    async def health_check(self) -> AgentStatus:
        """
        Check if agent is operational.
        
        Returns:
            Current agent status
        """
        pass
    
    async def can_handle(self, capability: AgentCapability) -> bool:
        """Check if agent supports a capability"""
        return capability in self.metadata.capabilities
```

---

### 2. Agent Registry

```python
from typing import Dict, Optional, List
import asyncio

class AgentRegistry:
    """
    Central registry for all available agents.
    
    Handles agent discovery, capability matching, and load balancing.
    """
    
    def __init__(self):
        self._agents: Dict[str, IAgent] = {}
        self._capability_index: Dict[AgentCapability, List[str]] = {}
    
    def register(self, agent: IAgent) -> None:
        """Register an agent with the system"""
        agent_id = agent.metadata.agent_id
        self._agents[agent_id] = agent
        
        # Index by capability for fast lookup
        for cap in agent.metadata.capabilities:
            if cap not in self._capability_index:
                self._capability_index[cap] = []
            self._capability_index[cap].append(agent_id)
    
    def unregister(self, agent_id: str) -> None:
        """Remove an agent from the system"""
        if agent_id in self._agents:
            agent = self._agents[agent_id]
            for cap in agent.metadata.capabilities:
                self._capability_index[cap].remove(agent_id)
            del self._agents[agent_id]
    
    def get_agent(self, agent_id: str) -> Optional[IAgent]:
        """Get specific agent by ID"""
        return self._agents.get(agent_id)
    
    def find_agents_for_capability(
        self, 
        capability: AgentCapability,
        exclude: List[str] = []
    ) -> List[IAgent]:
        """Find all agents that support a capability"""
        agent_ids = self._capability_index.get(capability, [])
        return [
            self._agents[aid] 
            for aid in agent_ids 
            if aid not in exclude
        ]
    
    async def get_best_agent(
        self, 
        capability: AgentCapability,
        prefer_fast: bool = False,
        prefer_cheap: bool = False
    ) -> Optional[IAgent]:
        """
        Select optimal agent for a capability.
        
        Considers: availability, response time, cost, current load
        """
        candidates = self.find_agents_for_capability(capability)
        
        if not candidates:
            return None
        
        # Filter to healthy agents
        healthy = []
        for agent in candidates:
            status = await agent.health_check()
            if status in [AgentStatus.IDLE, AgentStatus.WORKING]:
                healthy.append(agent)
        
        if not healthy:
            return None
        
        # Sort by preference
        if prefer_fast:
            healthy.sort(key=lambda a: a.metadata.avg_response_time_ms)
        elif prefer_cheap:
            healthy.sort(key=lambda a: a.metadata.cost_per_1k_tokens or float('inf'))
        
        return healthy[0]
    
    async def health_check_all(self) -> Dict[str, AgentStatus]:
        """Check health of all registered agents"""
        results = {}
        tasks = [
            (agent_id, agent.health_check()) 
            for agent_id, agent in self._agents.items()
        ]
        
        for agent_id, task in tasks:
            try:
                results[agent_id] = await asyncio.wait_for(task, timeout=5.0)
            except asyncio.TimeoutError:
                results[agent_id] = AgentStatus.OFFLINE
        
        return results
```

---

### 3. Task Orchestrator

```python
from typing import Callable, Awaitable
import uuid
import logging

logger = logging.getLogger("ultramind.orchestrator")

class TaskOrchestrator:
    """
    Central orchestration layer.
    
    Routes tasks to appropriate agents, handles fallbacks,
    and maintains execution state in Convex.
    """
    
    def __init__(
        self, 
        registry: AgentRegistry,
        state_store: 'ConvexClient',  # Your Convex connection
        insights_logger: 'InsightsLogger'
    ):
        self.registry = registry
        self.state = state_store
        self.insights = insights_logger
    
    async def execute_task(
        self,
        instruction: str,
        capability: AgentCapability,
        context: Dict[str, Any] = {},
        preferred_agent: Optional[str] = None,
        fallback_agents: List[str] = [],
        on_progress: Optional[Callable[[str], Awaitable[None]]] = None
    ) -> TaskResult:
        """
        Execute a task with automatic agent selection and fallback.
        
        Args:
            instruction: What to do
            capability: Type of work needed
            context: Current context from context.md/Convex
            preferred_agent: Try this agent first
            fallback_agents: Try these if preferred fails
            on_progress: Callback for progress updates
            
        Returns:
            TaskResult from successful agent or final error
        """
        task_id = str(uuid.uuid4())
        
        # Build request
        request = TaskRequest(
            task_id=task_id,
            instruction=instruction,
            capability=capability,
            context=context,
            fallback_agents=fallback_agents
        )
        
        # Log task start
        await self.state.log_task_start(task_id, request)
        
        # Determine agent order
        agents_to_try = []
        
        if preferred_agent:
            agent = self.registry.get_agent(preferred_agent)
            if agent and await agent.can_handle(capability):
                agents_to_try.append(agent)
        
        for fallback_id in fallback_agents:
            agent = self.registry.get_agent(fallback_id)
            if agent and await agent.can_handle(capability):
                agents_to_try.append(agent)
        
        # Add best available if we don't have enough options
        if len(agents_to_try) < 2:
            best = await self.registry.get_best_agent(
                capability,
                exclude=[a.metadata.agent_id for a in agents_to_try]
            )
            if best:
                agents_to_try.append(best)
        
        # Try each agent
        last_error = None
        for agent in agents_to_try:
            try:
                if on_progress:
                    await on_progress(f"Trying agent: {agent.metadata.name}")
                
                result = await agent.execute(request)
                
                if result.success:
                    # Log success
                    await self.state.log_task_complete(task_id, result)
                    
                    # Extract insights
                    if result.insights:
                        await self.insights.add_insights(result.insights)
                    
                    return result
                else:
                    last_error = result
                    logger.warning(
                        f"Agent {agent.metadata.agent_id} failed: {result.error}"
                    )
                    
            except Exception as e:
                logger.error(
                    f"Agent {agent.metadata.agent_id} exception: {str(e)}"
                )
                last_error = TaskResult(
                    success=False,
                    task_id=task_id,
                    agent_id=agent.metadata.agent_id,
                    capability_used=capability,
                    output=None,
                    duration_ms=0,
                    error=str(e),
                    error_code="EXCEPTION",
                    timestamp=datetime.utcnow()
                )
        
        # All agents failed
        await self.state.log_task_failed(task_id, last_error)
        await self.insights.add_insight(
            f"All agents failed for {capability}: {last_error.error if last_error else 'Unknown'}"
        )
        
        return last_error or TaskResult(
            success=False,
            task_id=task_id,
            agent_id="none",
            capability_used=capability,
            output=None,
            duration_ms=0,
            error="No agents available for capability",
            error_code="NO_AGENTS",
            timestamp=datetime.utcnow()
        )
    
    async def execute_workflow(
        self,
        steps: List[Dict[str, Any]],
        context: Dict[str, Any] = {}
    ) -> List[TaskResult]:
        """
        Execute a multi-step workflow (Flowgram).
        
        Each step's output becomes input context for next step.
        """
        results = []
        running_context = context.copy()
        
        for i, step in enumerate(steps):
            logger.info(f"Executing workflow step {i+1}/{len(steps)}: {step.get('name', 'unnamed')}")
            
            result = await self.execute_task(
                instruction=step['instruction'],
                capability=step['capability'],
                context=running_context,
                preferred_agent=step.get('agent'),
                fallback_agents=step.get('fallbacks', [])
            )
            
            results.append(result)
            
            if not result.success:
                if step.get('required', True):
                    logger.error(f"Required step failed, aborting workflow")
                    break
                else:
                    logger.warning(f"Optional step failed, continuing")
            else:
                # Add output to context for next step
                running_context[f"step_{i}_output"] = result.output
                if result.artifacts:
                    running_context[f"step_{i}_artifacts"] = result.artifacts
        
        return results
```

---

### 4. Concrete Agent Implementations

#### 4.1 Abacus AI Agent

```python
import httpx

class AbacusAgent(IAgent):
    """
    Abacus AI Deep Agent implementation.
    
    Primary use: App building, databases, production systems
    """
    
    def __init__(self, api_key: str, project_id: str):
        self._api_key = api_key
        self._project_id = project_id
        self._base_url = "https://api.abacus.ai/v1"
        self._client = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=300.0
        )
    
    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="abacus_deep_agent",
            name="Abacus AI Deep Agent",
            version="1.0.0",
            capabilities=[
                AgentCapability.BUILD,
                AgentCapability.DEPLOY,
                AgentCapability.ANALYZE
            ],
            max_concurrent_tasks=5,
            avg_response_time_ms=15000,
            cost_per_1k_tokens=0.01,
            requires_auth=True,
            supports_async=True,
            supports_streaming=True
        )
    
    async def execute(self, request: TaskRequest) -> TaskResult:
        start_time = datetime.utcnow()
        
        try:
            response = await self._client.post(
                f"{self._base_url}/agent/execute",
                json={
                    "project_id": self._project_id,
                    "instruction": request.instruction,
                    "context": request.context,
                    "timeout": request.timeout_seconds
                }
            )
            response.raise_for_status()
            data = response.json()
            
            duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            return TaskResult(
                success=True,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output=data.get("result"),
                artifacts=data.get("files_created", []),
                tokens_used=data.get("tokens_used"),
                duration_ms=duration,
                insights=data.get("learnings", []),
                timestamp=datetime.utcnow()
            )
            
        except httpx.HTTPStatusError as e:
            duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            return TaskResult(
                success=False,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output=None,
                duration_ms=duration,
                error=str(e),
                error_code=f"HTTP_{e.response.status_code}",
                fallback_suggested="agent_zero" if e.response.status_code >= 500 else None,
                timestamp=datetime.utcnow()
            )
    
    async def execute_async(self, request: TaskRequest) -> str:
        response = await self._client.post(
            f"{self._base_url}/agent/execute_async",
            json={
                "project_id": self._project_id,
                "instruction": request.instruction,
                "context": request.context,
                "callback_url": request.callback_url
            }
        )
        response.raise_for_status()
        return response.json()["job_id"]
    
    async def get_status(self, task_id: str) -> TaskResult:
        response = await self._client.get(
            f"{self._base_url}/agent/status/{task_id}"
        )
        response.raise_for_status()
        data = response.json()
        
        return TaskResult(
            success=data["status"] == "complete",
            task_id=task_id,
            agent_id=self.metadata.agent_id,
            capability_used=AgentCapability.BUILD,
            output=data.get("result"),
            artifacts=data.get("files_created", []),
            duration_ms=data.get("duration_ms", 0),
            error=data.get("error"),
            timestamp=datetime.utcnow()
        )
    
    async def cancel(self, task_id: str) -> bool:
        response = await self._client.post(
            f"{self._base_url}/agent/cancel/{task_id}"
        )
        return response.status_code == 200
    
    async def health_check(self) -> AgentStatus:
        try:
            response = await self._client.get(
                f"{self._base_url}/health",
                timeout=5.0
            )
            return AgentStatus.IDLE if response.status_code == 200 else AgentStatus.ERROR
        except:
            return AgentStatus.OFFLINE
```

#### 4.2 Agent Zero (Local Execution)

```python
import subprocess
import asyncio

class AgentZeroAgent(IAgent):
    """
    Agent Zero implementation for local OS operations.
    
    Primary use: Terminal commands, dependency management, file operations
    """
    
    def __init__(self, working_dir: str = "."):
        self._working_dir = working_dir
        self._running_tasks: Dict[str, asyncio.subprocess.Process] = {}
    
    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="agent_zero",
            name="Agent Zero (Local OS)",
            version="1.0.0",
            capabilities=[
                AgentCapability.EXECUTE,
                AgentCapability.DEPLOY
            ],
            max_concurrent_tasks=10,
            avg_response_time_ms=500,
            cost_per_1k_tokens=None,  # No token cost, runs locally
            requires_auth=False,
            supports_async=True,
            supports_streaming=True
        )
    
    async def execute(self, request: TaskRequest) -> TaskResult:
        start_time = datetime.utcnow()
        
        # Parse command from instruction
        command = self._parse_command(request.instruction)
        
        try:
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self._working_dir
            )
            
            stdout, stderr = await asyncio.wait_for(
                process.communicate(),
                timeout=request.timeout_seconds
            )
            
            duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            
            if process.returncode == 0:
                return TaskResult(
                    success=True,
                    task_id=request.task_id,
                    agent_id=self.metadata.agent_id,
                    capability_used=request.capability,
                    output=stdout.decode(),
                    duration_ms=duration,
                    timestamp=datetime.utcnow()
                )
            else:
                return TaskResult(
                    success=False,
                    task_id=request.task_id,
                    agent_id=self.metadata.agent_id,
                    capability_used=request.capability,
                    output=stdout.decode(),
                    duration_ms=duration,
                    error=stderr.decode(),
                    error_code=f"EXIT_{process.returncode}",
                    timestamp=datetime.utcnow()
                )
                
        except asyncio.TimeoutError:
            duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
            return TaskResult(
                success=False,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output=None,
                duration_ms=duration,
                error="Command timed out",
                error_code="TIMEOUT",
                timestamp=datetime.utcnow()
            )
    
    def _parse_command(self, instruction: str) -> str:
        """Extract shell command from natural language or direct command"""
        # If it looks like a direct command, use it
        if instruction.startswith(("npm ", "pip ", "git ", "cd ", "mkdir ", "rm ")):
            return instruction
        # Otherwise, this would integrate with an LLM to parse
        # For now, return as-is
        return instruction
    
    async def execute_async(self, request: TaskRequest) -> str:
        command = self._parse_command(request.instruction)
        
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=self._working_dir
        )
        
        self._running_tasks[request.task_id] = process
        return request.task_id
    
    async def get_status(self, task_id: str) -> TaskResult:
        process = self._running_tasks.get(task_id)
        if not process:
            return TaskResult(
                success=False,
                task_id=task_id,
                agent_id=self.metadata.agent_id,
                capability_used=AgentCapability.EXECUTE,
                output=None,
                duration_ms=0,
                error="Task not found",
                error_code="NOT_FOUND",
                timestamp=datetime.utcnow()
            )
        
        if process.returncode is None:
            # Still running
            return TaskResult(
                success=False,
                task_id=task_id,
                agent_id=self.metadata.agent_id,
                capability_used=AgentCapability.EXECUTE,
                output="Running...",
                duration_ms=0,
                timestamp=datetime.utcnow()
            )
        
        stdout, stderr = await process.communicate()
        return TaskResult(
            success=process.returncode == 0,
            task_id=task_id,
            agent_id=self.metadata.agent_id,
            capability_used=AgentCapability.EXECUTE,
            output=stdout.decode(),
            duration_ms=0,
            error=stderr.decode() if process.returncode != 0 else None,
            timestamp=datetime.utcnow()
        )
    
    async def cancel(self, task_id: str) -> bool:
        process = self._running_tasks.get(task_id)
        if process and process.returncode is None:
            process.terminate()
            return True
        return False
    
    async def health_check(self) -> AgentStatus:
        return AgentStatus.IDLE
```

#### 4.3 Manus AI Agent (Async Research)

```python
class ManusAgent(IAgent):
    """
    Manus AI implementation for async research tasks.
    
    Primary use: Deep research, competitor analysis, lead sourcing
    """
    
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._base_url = "https://api.manus.ai/v1"
        self._client = httpx.AsyncClient(
            headers={"X-API-Key": api_key},
            timeout=60.0
        )
    
    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="manus_research",
            name="Manus AI Research Agent",
            version="1.0.0",
            capabilities=[
                AgentCapability.RESEARCH,
                AgentCapability.ANALYZE
            ],
            max_concurrent_tasks=20,
            avg_response_time_ms=60000,  # Research takes time
            cost_per_1k_tokens=0.005,
            requires_auth=True,
            supports_async=True,
            supports_streaming=False
        )
    
    async def execute(self, request: TaskRequest) -> TaskResult:
        # Manus is async-first, so sync execution polls until complete
        job_id = await self.execute_async(request)
        
        start_time = datetime.utcnow()
        while True:
            result = await self.get_status(job_id)
            if result.success or result.error:
                return result
            
            elapsed = (datetime.utcnow() - start_time).total_seconds()
            if elapsed > request.timeout_seconds:
                await self.cancel(job_id)
                return TaskResult(
                    success=False,
                    task_id=request.task_id,
                    agent_id=self.metadata.agent_id,
                    capability_used=request.capability,
                    output=None,
                    duration_ms=int(elapsed * 1000),
                    error="Research timed out",
                    error_code="TIMEOUT",
                    timestamp=datetime.utcnow()
                )
            
            await asyncio.sleep(5)  # Poll every 5 seconds
    
    async def execute_async(self, request: TaskRequest) -> str:
        response = await self._client.post(
            f"{self._base_url}/research",
            json={
                "query": request.instruction,
                "depth": request.context.get("depth", "standard"),
                "sources": request.context.get("sources", ["web", "academic"]),
                "callback_url": request.callback_url
            }
        )
        response.raise_for_status()
        return response.json()["research_id"]
    
    async def get_status(self, task_id: str) -> TaskResult:
        response = await self._client.get(
            f"{self._base_url}/research/{task_id}"
        )
        response.raise_for_status()
        data = response.json()
        
        if data["status"] == "complete":
            return TaskResult(
                success=True,
                task_id=task_id,
                agent_id=self.metadata.agent_id,
                capability_used=AgentCapability.RESEARCH,
                output=data["findings"],
                artifacts=data.get("sources", []),
                duration_ms=data.get("duration_ms", 0),
                insights=[f"Research on: {data.get('query', 'unknown')}"],
                timestamp=datetime.utcnow()
            )
        elif data["status"] == "failed":
            return TaskResult(
                success=False,
                task_id=task_id,
                agent_id=self.metadata.agent_id,
                capability_used=AgentCapability.RESEARCH,
                output=None,
                duration_ms=data.get("duration_ms", 0),
                error=data.get("error", "Research failed"),
                error_code="RESEARCH_FAILED",
                timestamp=datetime.utcnow()
            )
        else:
            # Still running
            return TaskResult(
                success=False,
                task_id=task_id,
                agent_id=self.metadata.agent_id,
                capability_used=AgentCapability.RESEARCH,
                output=f"Progress: {data.get('progress', 0)}%",
                duration_ms=0,
                timestamp=datetime.utcnow()
            )
    
    async def cancel(self, task_id: str) -> bool:
        response = await self._client.delete(
            f"{self._base_url}/research/{task_id}"
        )
        return response.status_code == 200
    
    async def health_check(self) -> AgentStatus:
        try:
            response = await self._client.get(f"{self._base_url}/health")
            return AgentStatus.IDLE if response.status_code == 200 else AgentStatus.ERROR
        except:
            return AgentStatus.OFFLINE
```

#### 4.4 Pydantic AI Agent (Quality Control)

```python
class PydanticQAAgent(IAgent):
    """
    Pydantic AI implementation for quality assurance.
    
    Primary use: MMA Review loops, validation, self-annealing
    """
    
    def __init__(self, mma_config: Dict[str, Any]):
        self._config = mma_config
        self._thresholds = mma_config.get("thresholds", {
            "strategy_alignment": 8.0,
            "proof_discipline": 9.0,
            "cta_integrity": 9.0,
            "voice_consistency": 8.0,
            "clarity_structure": 8.0,
            "resonance": 8.0,
            "ethical_guardrails": 9.0
        })
    
    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="pydantic_qa",
            name="Pydantic AI Quality Controller",
            version="1.0.0",
            capabilities=[
                AgentCapability.VALIDATE,
                AgentCapability.ANALYZE
            ],
            max_concurrent_tasks=50,
            avg_response_time_ms=2000,
            cost_per_1k_tokens=0.002,
            requires_auth=False,
            supports_async=False,
            supports_streaming=False
        )
    
    async def execute(self, request: TaskRequest) -> TaskResult:
        start_time = datetime.utcnow()
        
        content = request.context.get("content")
        if not content:
            return TaskResult(
                success=False,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output=None,
                duration_ms=0,
                error="No content provided for validation",
                error_code="MISSING_CONTENT",
                timestamp=datetime.utcnow()
            )
        
        # Run MMA Review
        scores = await self._evaluate_dimensions(content, request.context)
        
        # Check against thresholds
        failures = []
        for dimension, score in scores.items():
            threshold = self._thresholds.get(dimension, 7.0)
            if score < threshold:
                failures.append({
                    "dimension": dimension,
                    "score": score,
                    "threshold": threshold,
                    "gap": threshold - score
                })
        
        duration = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        if not failures:
            return TaskResult(
                success=True,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output={
                    "verdict": "PASS",
                    "scores": scores,
                    "recommendation": "Content meets all quality thresholds"
                },
                duration_ms=duration,
                insights=[f"Quality check passed with avg score: {sum(scores.values())/len(scores):.1f}"],
                timestamp=datetime.utcnow()
            )
        else:
            return TaskResult(
                success=False,
                task_id=request.task_id,
                agent_id=self.metadata.agent_id,
                capability_used=request.capability,
                output={
                    "verdict": "FIX",
                    "scores": scores,
                    "failures": failures,
                    "recommendation": self._generate_fix_recommendations(failures)
                },
                duration_ms=duration,
                error=f"{len(failures)} dimensions below threshold",
                error_code="QUALITY_GATE_FAILED",
                fallback_suggested=None,  # No fallback for QA
                insights=[f"Quality failures in: {', '.join(f['dimension'] for f in failures)}"],
                timestamp=datetime.utcnow()
            )
    
    async def _evaluate_dimensions(
        self, 
        content: str, 
        context: Dict[str, Any]
    ) -> Dict[str, float]:
        """
        Evaluate content against MMA 7D dimensions.
        
        In production, this would call an LLM for sophisticated analysis.
        """
        # Simplified scoring logic - replace with actual LLM evaluation
        return {
            "strategy_alignment": 8.5,
            "proof_discipline": 9.2,
            "cta_integrity": 8.8,
            "voice_consistency": 8.1,
            "clarity_structure": 8.7,
            "resonance": 8.4,
            "ethical_guardrails": 9.5
        }
    
    def _generate_fix_recommendations(self, failures: List[Dict]) -> List[str]:
        """Generate specific fix recommendations for failed dimensions"""
        recommendations = []
        for failure in failures:
            dim = failure["dimension"]
            gap = failure["gap"]
            
            if dim == "proof_discipline":
                recommendations.append("Add specific statistics, case studies, or testimonials")
            elif dim == "voice_consistency":
                recommendations.append("Review brand voice guide and align tone throughout")
            elif dim == "ethical_guardrails":
                recommendations.append("Remove any manipulative urgency or unverified claims")
            # ... more recommendations per dimension
        
        return recommendations
    
    async def execute_async(self, request: TaskRequest) -> str:
        # QA is fast enough to run synchronously
        result = await self.execute(request)
        return request.task_id
    
    async def get_status(self, task_id: str) -> TaskResult:
        # Sync agent, status is always complete or not started
        return TaskResult(
            success=False,
            task_id=task_id,
            agent_id=self.metadata.agent_id,
            capability_used=AgentCapability.VALIDATE,
            output=None,
            duration_ms=0,
            error="Task not found or already complete",
            error_code="NOT_FOUND",
            timestamp=datetime.utcnow()
        )
    
    async def cancel(self, task_id: str) -> bool:
        return False  # Sync operations can't be cancelled
    
    async def health_check(self) -> AgentStatus:
        return AgentStatus.IDLE
```

---

## USAGE EXAMPLE

```python
async def main():
    # Initialize registry
    registry = AgentRegistry()
    
    # Register agents
    registry.register(AbacusAgent(
        api_key=os.environ["ABACUS_API_KEY"],
        project_id="ultramind_prod"
    ))
    registry.register(AgentZeroAgent(working_dir="./workspace"))
    registry.register(ManusAgent(api_key=os.environ["MANUS_API_KEY"]))
    registry.register(PydanticQAAgent(mma_config={}))
    
    # Initialize orchestrator
    orchestrator = TaskOrchestrator(
        registry=registry,
        state_store=ConvexClient(),
        insights_logger=InsightsLogger("./insights.md")
    )
    
    # Execute a single task with fallback
    result = await orchestrator.execute_task(
        instruction="Build a Stripe checkout page with React",
        capability=AgentCapability.BUILD,
        preferred_agent="abacus_deep_agent",
        fallback_agents=["agent_zero"]
    )
    
    if result.success:
        print(f"Built successfully: {result.artifacts}")
    else:
        print(f"Failed: {result.error}")
    
    # Execute a workflow (Flowgram)
    workflow_results = await orchestrator.execute_workflow(
        steps=[
            {
                "name": "Research competitors",
                "instruction": "Find top 5 competitor pricing pages",
                "capability": AgentCapability.RESEARCH,
                "agent": "manus_research"
            },
            {
                "name": "Build pricing page",
                "instruction": "Create pricing page based on research",
                "capability": AgentCapability.BUILD,
                "agent": "abacus_deep_agent"
            },
            {
                "name": "Quality check",
                "instruction": "Validate pricing page quality",
                "capability": AgentCapability.VALIDATE,
                "agent": "pydantic_qa"
            }
        ],
        context={"brand": "Freedomaker", "style": "modern"}
    )
    
    print(f"Workflow completed: {len([r for r in workflow_results if r.success])}/{len(workflow_results)} steps succeeded")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## EXTENSION POINTS

### Adding New Agents

```python
class NewAgentImplementation(IAgent):
    """Template for adding future agents"""
    
    @property
    def metadata(self) -> AgentMetadata:
        return AgentMetadata(
            agent_id="new_agent",
            name="New Agent",
            version="1.0.0",
            capabilities=[AgentCapability.BUILD],  # What it can do
            max_concurrent_tasks=10,
            avg_response_time_ms=5000,
            cost_per_1k_tokens=0.01,
            requires_auth=True,
            supports_async=True,
            supports_streaming=False
        )
    
    # Implement required methods...
```

### Custom Capabilities

```python
class CustomCapability(str, Enum):
    """Extend capabilities for domain-specific needs"""
    VOICE_SYNTHESIS = "voice_synthesis"
    VIDEO_GENERATION = "video_generation"
    FLOWGRAM_RENDER = "flowgram_render"
```

---

## FILE STRUCTURE

```
ultramind/
├── agents/
│   ├── __init__.py
│   ├── interface.py          # Base interfaces (IAgent, etc.)
│   ├── registry.py           # AgentRegistry
│   ├── orchestrator.py       # TaskOrchestrator
│   └── implementations/
│       ├── abacus.py
│       ├── agent_zero.py
│       ├── manus.py
│       ├── pydantic_qa.py
│       └── future_agents/
├── state/
│   ├── convex_client.py      # Convex integration
│   ├── insights_logger.py    # insights.md management
│   └── context_sync.py       # context.md sync
└── config/
    └── agent_config.yaml     # Agent credentials, thresholds
```

---

*Unified Agent Interface Specification v1.0.0*  
*ULTRAMIND Agentic Architecture*
