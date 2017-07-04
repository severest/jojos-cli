class Jojos < Formula
    include Language::Python::Virtualenv
    desc "jojojo"
    homepage "https://github.com/severest/jojos-cli"
    url "https://github.com/severest/jojos-cli/archive/0.3.0.tar.gz"

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
        sha256 "c6f3bdf4a4323ac7b45d01e04a6f6c20e32a052cd04de81e05103abc049ad9b9"
    end

    resource "requests-toolbelt" do
        url "https://files.pythonhosted.org/packages/86/f9/e80fa23edca6c554f1994040064760c12b51daff54b55f9e379e899cd3d4/requests-toolbelt-0.8.0.tar.gz"
        sha256 "f6a531936c6fa4c6cfce1b9c10d5c4f498d16528d2a54a22ca00011205a187b5"
    end

    resource "urllib3" do
        url "https://files.pythonhosted.org/packages/96/d9/40e4e515d3e17ed0adbbde1078e8518f8c4e3628496b56eb8f026a02b9e4/urllib3-1.21.1.tar.gz"
        sha256 "b14486978518ca0901a76ba973d7821047409d7f726f22156b24e83fd71382a5"
    end

    resource "chardet" do
        url "https://files.pythonhosted.org/packages/fc/bb/a5768c230f9ddb03acc9ef3f0d4a3cf93462473795d18e9535498c8f929d/chardet-3.0.4.tar.gz"
        sha256 "84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae"
    end

    resource "certifi" do
        url "https://files.pythonhosted.org/packages/dd/0e/1e3b58c861d40a9ca2d7ea4ccf47271d4456ae4294c5998ad817bd1b4396/certifi-2017.4.17.tar.gz"
        sha256 "f7527ebf7461582ce95f7a9e03dd141ce810d40590834f4ec20cddd54234c10a"
    end

    resource "idna" do
        url "https://files.pythonhosted.org/packages/d8/82/28a51052215014efc07feac7330ed758702fc0581347098a81699b5281cb/idna-2.5.tar.gz"
        sha256 "3cb5ce08046c4e3a560fc02f138d0ac63e00f8ce5901a56b32ec8b7994082aab"
    end

    def install
        virtualenv_install_with_resources
    end
end
