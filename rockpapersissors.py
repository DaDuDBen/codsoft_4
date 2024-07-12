from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random
class RockPaperScissorsGame(App):
    def build(self):
        self.title = 'Rock Paper Scissors Game'
        self.user_score = 0
        self.comp_score = 0   
        self.user_choice_label = Label(text="Choose:")
        self.comp_choice_label = Label(text="Computer chose: ")
        self.result_label = Label(text="")
        self.score_label = Label(text=f"Score: You {self.user_score} - {self.comp_score} Computer")        
        self.rock_button = Button(text="Rock", on_press=lambda x: self.on_choice('rock'))
        self.paper_button = Button(text="Paper", on_press=lambda x: self.on_choice('paper'))
        self.scissors_button = Button(text="Scissors", on_press=lambda x: self.on_choice('scissors'))        
        button_layout = BoxLayout(orientation='horizontal')
        button_layout.add_widget(self.rock_button)
        button_layout.add_widget(self.paper_button)
        button_layout.add_widget(self.scissors_button)        
        self.play_again_button = Button(text="Play Again", on_press=self.play_again)        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.user_choice_label)
        layout.add_widget(button_layout)
        layout.add_widget(self.comp_choice_label)
        layout.add_widget(self.result_label)
        layout.add_widget(self.score_label)
        layout.add_widget(self.play_again_button)
        return layout
    def play_again(self, instance):
        self.user_choice_label.text = "Choose:"
        self.comp_choice_label.text = "Computer chose: "
        self.result_label.text = ""
        self.score_label.text = f"Score: You {self.user_score} - {self.comp_score} Computer"
    def on_choice(self, choice):
        self.user_choice_label.text = f"You chose: {choice.capitalize()}"
        choices = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(choices)
        self.comp_choice_label.text = f"Computer chose: {comp_choice.capitalize()}"        
        result = self.determine_winner(choice, comp_choice)      
        self.result_label.text = result        
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.comp_score += 1       
        self.score_label.text = f"Score: You {self.user_score} - {self.comp_score} Computer"
    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper') or \
             (user_choice == 'paper' and comp_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"
if __name__ == '__main__':
    RockPaperScissorsGame().run()
