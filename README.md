# rofi-taskwarrior
Rofi with taskwarrior for i3wm. WIP

## Usage example i3

#### Show input to add task to taskwarrior
bindsym $mod+t exec $HOME/.config/i3/scripts/tasks/main.py

#### Manage tasks
bindsym $mod+y exec "$HOME/.config/i3/scripts/tasks/main.py list"
