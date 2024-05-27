# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Production(Package):
    """Bash and FHICL scripts for Mu2e offline reco and simulation"""

    homepage = "https://github.com/Mu2e/Production"
    url = "https://github.com/Mu2e/Production/archive/refs/tags/v00_21_00.tar.gz"
    git = "https://github.com/Mu2e/Production"
    maintainers = ["brownd1978","kutschke","rlcee"]

    version("main", branch="main")
    version("0.21.0", sha256="e4330546549f3c18d286f2772d6e31e0bffb4b0e103708f323e5a8692dd1e124")


    def url_for_version(self, version):
        url = "https://github.com/Mu2e/Production/archive/refs/tags/v{:d}_{:d}_{:d}.tar.gz"
        aa = str(version.dotted).split('.')
        return url.format(int(aa[0]),int(aa[1]),int(aa[2]))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(self.stage.source_path + "/Scripts/*.sh", prefix.bin)
        install(self.stage.source_path + "/Scripts/POMS/*.sh", prefix.bin)
        for dd in ["JobConfig","Processing","Tests","Validation"] :
            install_tree(self.stage.source_path + "/" + dd,
                         prefix + "/fcl/Production/" + dd)
        install_tree(self.stage.source_path + "/CampaignConfig",
                     prefix + "/share/CampaignConfig/" )

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
