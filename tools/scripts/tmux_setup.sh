#!/bin/bash
# SUPERMIND TMUX Layout v1.0.0
# Run via WSL: wsl bash /mnt/c/Users/cfar7/OneDrive/Desktop/ULTRAMIND/tools/scripts/tmux_setup.sh

SESSION_NAME="supermind"
ULTRAMIND_PATH="/mnt/c/Users/cfar7/OneDrive/Desktop/ULTRAMIND"

# Kill existing session if it exists
tmux kill-session -t $SESSION_NAME 2>/dev/null

# Create new session
tmux new-session -d -s $SESSION_NAME -c "$ULTRAMIND_PATH"

# Rename first window
tmux rename-window -t $SESSION_NAME:0 'main'

# Split into 4 panes
#  ┌────────────────┬────────────────┐
#  │                │    STATE       │
#  │     CLAUDE     ├────────────────┤
#  │                │    LOGS        │
#  ├────────────────┴────────────────┤
#  │            GIT / TOOLS          │
#  └─────────────────────────────────┘

# Main pane (left) - for Claude Code
tmux send-keys -t $SESSION_NAME "cd $ULTRAMIND_PATH && clear" C-m

# Right pane - split vertically
tmux split-window -h -t $SESSION_NAME -c "$ULTRAMIND_PATH"
tmux send-keys -t $SESSION_NAME "watch -n 5 'python tools/scripts/session_state.py show'" C-m

# Bottom-right pane - logs
tmux split-window -v -t $SESSION_NAME -c "$ULTRAMIND_PATH"
tmux send-keys -t $SESSION_NAME "tail -f /tmp/supermind.log 2>/dev/null || echo 'No logs yet. Touch /tmp/supermind.log to start.'" C-m

# Bottom pane - git/tools (full width)
tmux select-pane -t $SESSION_NAME:0.0
tmux split-window -v -t $SESSION_NAME -c "$ULTRAMIND_PATH"
tmux send-keys -t $SESSION_NAME "git status && echo '' && python tools/scripts/canvas.py state" C-m

# Resize panes
tmux resize-pane -t $SESSION_NAME:0.0 -x 60%  # Main Claude pane
tmux resize-pane -t $SESSION_NAME:0.1 -x 40%  # State pane
tmux resize-pane -t $SESSION_NAME:0.3 -y 10   # Bottom tools pane

# Select main pane
tmux select-pane -t $SESSION_NAME:0.0

# Attach to session
tmux attach-session -t $SESSION_NAME

echo "SUPERMIND TMUX session started: $SESSION_NAME"
echo "Panes: Claude (main) | State Monitor | Logs | Git/Tools"
