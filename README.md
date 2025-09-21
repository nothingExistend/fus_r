# noStream

## requirements

- python modules
  - requests
  - pywebview
 
- system (expected)
  - 40 MB storage
  - 2 GB RAM (not sure! but with several services in background possible)
 
## concept
- pywebview is used to open several streaming services in the background without giving the user access to them
- a sepperate app opens that connects via an API to each of those services
- over the API's the app is capable of functioning as a remote control for the streaming services in the background
- python is used for backend code and pywebview is used for frontend code and UI
- the user is capable of interacting with this app to controll the background services to play music
- the user is capable of creating playlists across multiple platforms in one app with "Cross-Playlisting"

## roadmap

- creating pywebview application
- installer/update programm for dependencies
- porting for Android and Linux
- Recreating for iOS (💀)
