package main

import (
	"fmt"
	"log"
    "os"
	"os/exec"
    "regexp"
)

func main() {
    // look for binaries
    git_path, err := exec.LookPath("git")
	if err != nil {
        fmt.Println("You need to install git")
        os.Exit(1)
	}
    hub_path, err := exec.LookPath("hub")
	if err != nil {
        fmt.Println("You need to install hub, (use Homebrew)")
        os.Exit(1)
	}

    // check args
    jojo_regex := regexp.MustCompile("jojos")
    if !jojo_regex.MatchString(os.Args[0]) {
        fmt.Println("Y U NO JOJO??")
        os.Exit(1)
    }
    if len(os.Args) < 2 {
        fmt.Println("Need an issues number as an argument")
        os.Exit(1)
    }
    issue_number := os.Args[1]


	out, err := exec.Command(fmt.Sprintf("%s", git_path), "branch", "-a").Output()
	if err != nil {
		log.Fatal(err)
	}


    branch_regex := regexp.MustCompile(fmt.Sprintf("remotes/origin/issues/%s", issue_number))
    fmt.Printf("%q\n", branch_regex.FindString(fmt.Sprintf("%s", out)))

    out2, err := exec.Command(fmt.Sprintf("%s", hub_path)).Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s", out2)
}
