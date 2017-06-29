require "formula"

class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/master.tar.gz"
    version "0.1.0"

    def install
        virtualenv_install_with_resources
    end
end
