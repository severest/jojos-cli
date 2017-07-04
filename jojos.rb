class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/0.2.2.tar.gz"

    resource "docopt" do
        url "https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz"
        sha256 "49b3a825280bd66b3aa83585ef59c4a8c82f2c8a522dbe754a8bc8d08c85c491"
    end

    resource "PyGithub" do
        url "https://files.pythonhosted.org/packages/43/cb/35fbf0e380595dab7720e6b4a9f8f19c5947b90e84fa23b7cedea945222e/PyGithub-1.34.tar.gz"
        sha256 "a9ad589a325b433eb8917d5675d7bafd54266607ffe778e5a3115a1b0caf41b8"
    end

    resource "PyYAML" do
        url "https://files.pythonhosted.org/packages/4a/85/db5a2df477072b2902b0eb892feb37d88ac635d36245a72a6a69b23b383a/PyYAML-3.12.tar.gz"
        sha256 "592766c6303207a20efc445587778322d7f73b161bd994f227adaa341ba212ab"
    end

    resource "PyJWT" do
        url "https://files.pythonhosted.org/packages/ac/b2/72a8bff872e6f8e2aed4f4210aa24ba9c9f4f03a67f34e2f867905122235/PyJWT-1.5.2.tar.gz"
        sha256 "1179f0bff86463b5308ee5f7aff1c350e1f38139d62a723e16fb2c557d1c795f"
    end

    resource "requests" do
        url "https://files.pythonhosted.org/packages/2c/b5/2b6e8ef8dd18203b6399e9f28c7d54f6de7b7549853fe36d575bd31e29a7/requests-2.18.1.tar.gz"
        sha256 "jjojojo"
    end

    resource "requests-toolbelt" do
        url "https://files.pythonhosted.org/packages/86/f9/e80fa23edca6c554f1994040064760c12b51daff54b55f9e379e899cd3d4/requests-toolbelt-0.8.0.tar.gz"
        sha256 "f6a531936c6fa4c6cfce1b9c10d5c4f498d16528d2a54a22ca00011205a187b5"
    end

    def install
        virtualenv_install_with_resources
    end
end
