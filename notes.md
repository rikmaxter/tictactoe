
## UI

- `window` : main window, provides OS border, close button, title bar
- `frame` : groups and organizes child widgets (buttons, labels).

```
window
├── top_frame
│   ├── selection_frame          
│   │   ├── label ("Choose your symbol:")
│   │   └── btn_frame
│   │       ├── button "O"
│   │       └── button "X"
│   ├── status (tour)
│   └── play_again_btn    
|       
└── board_frame
    ├── button (0,0)
    ├── button (0,1)
    └── button ...
```