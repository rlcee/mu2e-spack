# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


def sanitize_environments(env, *vars):
    for var in vars:
        env.prune_duplicate_paths(var)
        env.deprioritize_system_paths(var)

class Offline(CMakePackage):
    """The Mu2e Offline analysis code suite"""

    homepage = "https://mu2e.fnal.gov"
    git = "https://github.com/Mu2e/Offline"

    maintainers("eflumerf", "kutschke", "rlcee")

    license("Apache-2.0")

    version("main", branch="main", get_full_repo=True)
    version("11.00.01", commit="67f7904d5")
    version("11.01.00", commit="1560c76")

    variant("g4", default=False, description="Whether to build Geant4-dependent packages")

    # Direct dependencies, see ups/product_deps
    depends_on("geant4", when="+g4")
    depends_on("cetmodules", type="build")
    depends_on("artdaq-core-mu2e")
    depends_on("art-root-io")
    depends_on("kinkal")
    depends_on("btrk")
    depends_on("gallery")
    depends_on("cry", when="+g4")
    depends_on("swig", type="build")
    depends_on("gsl")
    depends_on("xerces-c")

    # Indirect dependencies (But still required by CMake)
    depends_on("postgresql")
    depends_on("openblas")
    depends_on("root+tmva-sofie+spectrum")

    def cmake_args(self):
        args = ["-DWANT_G4={0}".format("TRUE" if "+g4" in self.spec else "FALSE")]
        return args

    def setup_run_environment(self, env):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        env.prepend_path("MU2E_SEARCH_PATH", prefix + "/fcl")
        # Ensure we can find data files
        env.prepend_path("MU2E_DATA_PATH", prefix + "/share")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH", "MU2E_SEARCH_PATH", "MU2E_DATA_PATH")

    def setup_dependent_run_environment(self, env, dependent_spec):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        env.prepend_path("MU2E_SEARCH_PATH", prefix + "/fcl")
        # Ensure we can find data files
        env.prepend_path("MU2E_DATA_PATH", prefix + "/share")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH", "MU2E_SEARCH_PATH", "MU2E_DATA_PATH")
