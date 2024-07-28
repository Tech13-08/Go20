# Go20

A program to help you in following the 20-20-20 rule: Look 20 feet away for 20 seconds every 20 minutes.

## Getting Started

### Dependencies

* None! Besides an OS of course: Windows/MacOS/Linus are all fine as long as it can handle automating tasks.

### Installing

* Click the `main.exe` file and download it. 

### Executing program

- Windows
> * Open the `Task Scheduler` using the search or start menu.
> * Create a `new task` and follow this template for the setup
>
> 
>  * The only important setting here is the `Run only when user is logged on`. This must be enabled or else you won't see the window. The other settings on this tab are up to preference.
>   
>   <img src="https://github.com/Tech13-08/Go20/assets/68032044/a8ddb339-ac83-4af2-94b6-a7769fc98890" width="400" height="300">

>   
>   
> *  Under the `Trigger` tab, make a new trigger and follow every setting here exactly as shown. The goal is to repeat the task every 20 minutes automatically.
>   
>  <img src="https://github.com/Tech13-08/Go20/assets/68032044/31e317d3-a6b5-4d90-917e-bfe1debf1954" width="800" height="300">

> 
>   
>  * Here, the action will be starting a program, simply paste the location of the `main.exe` you installed earlier.
>   
>  <img src="https://github.com/Tech13-08/Go20/assets/68032044/4df4e755-0157-4cad-8967-5a613b75827e" width="400" height="300">
> 
>
> 
> * That's it! Everything should work automatically now. If you see nothing, right click the tast you just made and click `run` just in case.
> * If you ever want to disable/enable this program, that is also an option found by right clicking the task you just made.
>
- Mac OS
> * Coming soon
>   
- Linux
> * Coming soon


### My Progress
> Go20 yielded on average an hour reduction in screen time per day

* Screen Time throughout week before using Go20:

  <img src="https://github.com/Tech13-08/Go20/assets/68032044/ed93aa1d-a68e-4823-bc32-fb9ba65d69f6" width="600" height="500">

* Screen Time throughout week after using Go20:
  
  <img src="https://github.com/user-attachments/assets/b553081c-25d6-4075-adf8-aff03fe37b0d" width="600" height="500">
  

> The screen time monitoring code was made in python using matplotlib for the graphing and psutil for the screen time. The code is also available in this repository, however it is not neccessary for running Go20. If you would also like to monitor your screen time with this code, follow these steps:
> * Download the 3 python files and 2 bat files into the same directory
> * Set up tasks using the `Task Scheduler` for each of the bat files. Make sure in the `Action` tab, when you set the path to the bat file, you also fill out the `Start in (optional)` field with the path to the directory you put all the files in.
> * For the screen monitoring bat file, have it run every minute indefenitely and for the screen update bat file, have it run every day at 12 am.
> * To check you progress, simply look at the log and text files created in the same directory you put the python and bat files in.
> * The generate graph python file can be used to make the graph for the screen time hours. 



## Authors

- Falak Tulsi  [Tech13-08](https://github.com/Tech13-08)
  
## License

This project is licensed under the MIT License - see the LICENSE.md file for details
