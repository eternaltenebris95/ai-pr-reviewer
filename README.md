# ai-pr-reviewer

Using AI to analyze push/pull of git hub request

1. TEST GIT HUB ACCESS FROM LINUX -- DONE 12/29
	- Install GIT on Linux or Similar CLI: 
		sudo apt install git
	- Create a project folders: 
		mkdir ai-pr-reviewer
		cd ai-pr-reviewer
		git init
	- Create an SSH key: 
		ssh-keygen -t ed25519 -C "you@example.com"
	- Start the SSH agent & add your key: 
		eval "$(ssh-agent -s)"
		ssh-add ~/.ssh/id_ed25519
	- Add the SSH key to Github:
		cat ~/.ssh/id_ed25519.pub
	- Copy the output and paste it into GitHub → Settings → SSH and GPG keys → New SSH Key.
	- Create a repository on GITHUB as ai-pr-reviewer
	- Cloning SSH:
		git clone git@github.com:username/repo.git
	- Push your code:
		git add .
		git commit -m "Initial commit"
		git push -u origin main 

2.
# test
