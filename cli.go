package main

import (
	"flag"
	"fmt"
	"io"
	"bufio"
	"os"
	"os/exec"
	"regexp"
	"strings"
)

// Exit codes are int values that represent an exit code for a particular error.
const (
	ExitCodeOK    int = 0
	ExitCodeError int = 1 + iota
)

// CLI is the command line object
type CLI struct {
	// outStream and errStream are the stdout and stderr
	// to write message from the CLI.
	outStream, errStream io.Writer
}

// Run invokes the CLI with the given arguments.
func (cli *CLI) Run(args []string) int {
	var (
		issueNumber int
		issueString string
		version bool
	)

	// Define option flag parse
	flags := flag.NewFlagSet(Name, flag.ContinueOnError)
	flags.SetOutput(cli.errStream)

	flags.IntVar(&issueNumber, "i", 0, "The issue number you wish to create a PR for")

	flags.BoolVar(&version, "version", false, "Print version information and quit.")

	// Parse commandline flag
	if err := flags.Parse(args[1:]); err != nil {
		return ExitCodeError
	}

	// Show version
	if version {
		fmt.Fprintf(cli.errStream, "%s version %s\n", Name, Version)
		return ExitCodeOK
	}

	// check for mandatory issue number
	if issueNumber == 0 {
		fmt.Fprintln(cli.errStream, "You must use -i to input an issue number")
		return ExitCodeError
	}
	issueString = fmt.Sprintf("issues/%d", issueNumber)


	// look for binaries
    gitPath, err := exec.LookPath("git")
	if err != nil {
        fmt.Fprintln(cli.errStream, "You need to install git")
        return ExitCodeError
	}
    hubPath, err := exec.LookPath("hub")
	if err != nil {
        fmt.Fprintln(cli.errStream, "You need to install hub, (use Homebrew)")
        return ExitCodeError
	}

	// check args
    jojoRegex := regexp.MustCompile("jojos")
    if !jojoRegex.MatchString(os.Args[0]) {
        fmt.Fprintf(cli.outStream, "Y U NO JOJOS?? I'm very disappointed in you....\n\n\n")
    }


	fmt.Fprintf(cli.outStream, "Checking out staging...\n")
	_, err = exec.Command(string(gitPath[:]), "checkout", "staging").Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Searching git branches failed. Ensure you are in a git repository. Git: %s\n", err)
		return ExitCodeError
	}
	fmt.Fprintf(cli.outStream, "Fetching all remote branches...\n")
	_, err = exec.Command(string(gitPath[:]), "fetch").Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "git fetch failed. Ensure you are in a git repository. Git: %s\n", err)
		return ExitCodeError
	}
	fmt.Fprintf(cli.outStream, "Searching for branch name...")
	branchesList, err := exec.Command(string(gitPath[:]), "branch", "-a").Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Searching git branches failed. Ensure you are in a git repository. Git: %s\n", err)
		return ExitCodeError
	}

	var branchName string
	branchSuffix := 0
	branchFound := true
	for branchFound {
		branchSuffix++
		branchName = fmt.Sprintf("%s-%d", issueString, branchSuffix)
		branchRegex := regexp.MustCompile(branchName)
		fmt.Fprintf(cli.outStream, "%d..", branchSuffix)
		regexResults := branchRegex.FindString(string(branchesList[:]))
		if regexResults == "" {
			branchFound = false
		}
	}

	fmt.Fprintf(cli.outStream, "\nCreating pull-request: %s\n", branchName)

	_, err = exec.Command(string(gitPath[:]), "checkout", "-b", branchName).Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Creating a new branch failed. Git: %s\n", err)
		return ExitCodeError
	}
	_, err = exec.Command(string(gitPath[:]), "commit", "-m", fmt.Sprintf("Connect to issue #%d\n\n[ci skip]", issueNumber), "--allow-empty").Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Commiting failed. Git: %s\n", err)
		return ExitCodeError
	}
	_, err = exec.Command(string(gitPath[:]), "push", "-u", "origin", branchName).Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Pushing the new branch failed. Git: %s\n", err)
		return ExitCodeError
	}

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter PR title: ")
	prTitle, _ := reader.ReadString('\n')
    prURL, err := exec.Command(string(hubPath[:]), "pull-request", "-m", prTitle).Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Creating a pull-request failed: %s\n", err)
		return ExitCodeError
	}

	fmt.Fprintf(cli.outStream, "ALL DONE! %s", prURL)
	_, err = exec.Command("open", strings.Trim(string(prURL[:]), "\n")).Output()
	if err != nil {
		fmt.Fprintf(cli.errStream, "Trying to open the PR failed: %s\n", err)
		return ExitCodeError
	}

	return ExitCodeOK
}
