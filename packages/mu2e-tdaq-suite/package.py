# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *

class Mu2eTdaqSuite(BundlePackage):
    """The Mu2e TDAQ Suite, the software used for Mu2e trigger and data acquisition
    """

    version("develop")
    version("v1_04_00")
    version("v1_02_03")
    version("v1_02_02")
    
    squals = ("112", "117", "118", "122", "123", "126", "128")
    variant(
        "s",
        default="0",
        values=("0",) + squals,
        multi=False,
        description="Art suite version to use",
    )
    for squal in squals:
        depends_on(f"art-suite@s{squal}+root", when=f"s={squal}")
    depends_on("art-suite+root", when="s=0")

    variant(
        "artdaq",
        default="0",
        values = ("0","31202","31203", "31207"),
        multi=False,
        description="Artdaq suite version to use",
    )   
    depends_on("artdaq-suite@v3_12_07", when="artdaq=31207")
    depends_on("artdaq-suite@v3_12_03", when="artdaq=31203")
    depends_on("artdaq-suite@v3_12_02", when="artdaq=31202")
    depends_on("artdaq-suite+db+epics~demo~pcp")

    variant("otsdaq",
            default="0",
            values = ("0", "20608", "20609", "20700"),
            multi=False,
            description="Otsdaq version to use",
    )
    depends_on("otsdaq-suite@v2_07_00", when="otsdaq=20700")
    depends_on("otsdaq-suite@v2_06_09", when="otsdaq=20609")
    depends_on("otsdaq-suite@v2_06_08", when="otsdaq=20608")
    depends_on("otsdaq-suite")

    with when("@v1_04_00"):
        depends_on("artdaq-core-mu2e@v2_01_02")
        depends_on("mu2e-pcie-utils@v2_09_01")
        depends_on("artdaq-mu2e@v1_07_00")
        depends_on("otsdaq-mu2e@v1_04_00")
        depends_on("otsdaq-mu2e-calorimeter@v1_04_00")
        depends_on("otsdaq-mu2e-crv@v1_04_00")
        depends_on("otsdaq-mu2e-extmon@v1_04_00")
        depends_on("otsdaq-mu2e-stm@v1_04_00")
        #depends_on("otsdaq-mu2e-tracker@v1_04_00")
        depends_on("Offline@11.00.01")
        depends_on("otsdaq-mu2e-dqm@v1_04_00")
        depends_on("otsdaq-mu2e-trigger@v1_04_00")
    with when("@v1_02_02"):
        depends_on("mu2e-pcie-utils@v2_08_00")
        depends_on("artdaq-core-mu2e@v1_08_04")
        depends_on("artdaq-mu2e@v1_05_02")
        depends_on("otsdaq-mu2e@v1_02_02")
        
    with when("@develop"):
        depends_on("artdaq-core-mu2e@develop")
        depends_on("mu2e-pcie-utils@develop")
        depends_on("artdaq-mu2e@develop")
        depends_on("otsdaq-mu2e@develop")
        depends_on("otsdaq-mu2e-calorimeter@develop")
        depends_on("otsdaq-mu2e-crv@develop")
        depends_on("otsdaq-mu2e-extmon@develop")
        depends_on("otsdaq-mu2e-stm@develop")
        depends_on("otsdaq-mu2e-tracker@develop")
        depends_on("Offline@main")
        depends_on("otsdaq-mu2e-dqm@develop")
        depends_on("otsdaq-mu2e-trigger@develop")
