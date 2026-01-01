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

2. FIXING DOCKERFILE 12/30
	- Installing Docker on Linux
	- Update existing packages
		sudo apt-get update
	- Install prerequisite packages
		sudo apt-get install ca-certificates curl gnupg
	- Add Docker’s official GPG key
		sudo install -m 0755 -d /etc/apt/keyrings
		curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
		sudo chmod a+r /etc/apt/keyrings/docker.gpg
	- Setup the Docker repository
		echo \
  			"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  			$(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" | \
  			sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	- Install Docker Engine and CLI
		sudo apt-get update
		sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
	- Check Docker version
		docker --version

# trigger AI
