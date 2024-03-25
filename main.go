package main

import (
	"image/color"
	"time"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
	"github.com/gen2brain/beeep"
)

func main() {
	a := app.New()
	w := a.NewWindow("Go20")
	width, height := float32(1920), float32(1080)
	w.Resize(fyne.NewSize(width, height))
	w.SetFixedSize(true)

	// Create the message label
	message := canvas.NewText("It has been 20 minutes, please take a 20 second break and look 20 feet away.", color.White)
	message.Alignment = fyne.TextAlignCenter
	message.TextStyle = fyne.TextStyle{Bold: true} // Optional: make the text bold
	message.TextSize = height / 40

	// Create the message label
	beepMessage := canvas.NewText("The system will make a beep after the break duration.", color.White)
	beepMessage.Alignment = fyne.TextAlignCenter
	beepMessage.TextStyle = fyne.TextStyle{Bold: true} // Optional: make the text bold
	beepMessage.TextSize = height / 40

	// Create the "Quit" button
	quitButton := widget.NewButton("Quit", func() {
		w.Close()
	})

	// Create a container to hold the message and the button
	content := container.NewVBox(
		message,
		beepMessage,
		layout.NewSpacer(),
		container.NewHBox(
			layout.NewSpacer(),
			quitButton,
			layout.NewSpacer(),
		),
	)

	// Use a CenterLayout to center the content both horizontally and vertically
	centeredContent := container.New(layout.NewCenterLayout(), content)

	// Set the content of the window
	w.SetContent(centeredContent)

	go func() {
		w.Show()
		go func() {
			time.Sleep(20 * time.Second)
			beeep.Beep(beeep.DefaultFreq, beeep.DefaultDuration)
			w.Close()
		}()
		for {
			w.RequestFocus()
			w.CenterOnScreen()
		}
	}()

	a.Run()
}
