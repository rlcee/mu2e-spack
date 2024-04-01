# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

def sanitize_environments(env, *vars):
    for var in vars:
        env.prune_duplicate_paths(var)
        env.deprioritize_system_paths(var)

class OtsdaqMu2eCalorimeter(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://mu2e.fnal.gov"
    git = "https://github.com/Mu2e/otsdaq_mu2e_calorimeter.git"
    url = "https://github.com/Mu2e/otsdaq_mu2e_calorimeter/archive/refs/tags/v1_04_00.tar.gz"

    maintainers("eflumerf", "rrivera747")

    license("BSD")

    version("develop", branch="develop", get_full_repo=True)
    version("v3_00_00", sha256="fd99f653a708d23e2f8d7328bc3dbdf2b9f242f9ce19f5a3ef400485be6954b3")
    version("v1_04_00", sha256="7df9ff2c6f1cdf5d13b7b744b38c24f1e7901c7fac07dc64ccacd80736cea5fa")

    def url_for_version(self, version):
        url = "https://github.com/Mu2e/otsdaq_mu2e_calorimeter/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    depends_on("otsdaq-mu2e")
    depends_on("cetmodules", type="build")

    def setup_run_environment(self, env):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")

    def setup_dependent_run_environment(self, env, dependent_spec):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")
