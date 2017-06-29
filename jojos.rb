class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/0.1.3.tar.gz"

    resource "docopt" do
        url "https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz"
        sha256 "49b3a825280bd66b3aa83585ef59c4a8c82f2c8a522dbe754a8bc8d08c85c491"
    end

    resource "PyGithub" do
        url "https://files.pythonhosted.org/packages/43/cb/35fbf0e380595dab7720e6b4a9f8f19c5947b90e84fa23b7cedea945222e/PyGithub-1.34.tar.gz"
        sha256 "jojos"
    end

    def install
        virtualenv_install_with_resources
    end
end
