#!/bin/bash

session="mud_client"

setup_session () {

    echo "Creating session: $session"

    # start a new session with our name
    tmux new-session -d -s $session -n "client"

    # setup the first window
    tmux send-keys -t $session:"client" "tail -f achaea.log" C-m

    # make the right side
    # the proxy
    tmux split-window -h -l 5 -t $session:"client"
    tmux send-keys -t $session:"client".2 "python3.8 proxy.py -L 127.0.0.1:8888:67.202.114.4:23"
    # fighting log
    tmux split-window -v -l 80 -t $session:"client".2
    tmux send-keys -t $session:"client".3 "tail -f says.log" C-m
    # notes
    tmux split-window -v -l 50 -t $session:"client".3
    tmux send-keys -t $session:"client".4 "vim notes/todo.md" C-m

    # make the prompt part
    tmux split-window -v -l 5 -t $session:"client".1
    tmux send-keys -t $session:"client".2 "python3 client.py"

}


# Check if the session exists, discarding output
# We can check $? for the exit status (zero for success, non-zero for failure)
tmux has-session -t $session 2>/dev/null

if [ $? != 0 ]; then
    # Set up your session
    setup_session
else
    echo "$session already exists!"
fi

tmux attach-session -t $session:1
