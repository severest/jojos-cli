require "formula"

class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/v0.1.1.tar.gz"
    version "0.1.1"

    resource "docopt" do
        url "https://pypi.python.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz"
    end

    def install
        virtualenv_install_with_resources
    end
end
