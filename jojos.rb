require "formula"

class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/0.1.2.tar.gz"
    version "0.1.2"

    resource "docopt" do
        url "https://pypi.python.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz"
        sha256 "49b3a825280bd66b3aa83585ef59c4a8c82f2c8a522dbe754a8bc8d08c85c491"
    end

    def install
        virtualenv_install_with_resources
    end
end
