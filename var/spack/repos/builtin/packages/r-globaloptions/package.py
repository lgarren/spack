##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RGlobaloptions(RPackage):
    """It provides more controls on the option values such as validation and
       filtering on the values, making options invisible or private."""

    homepage = "https://cran.r-project.org/package=GlobalOptions"
    url      = "https://cran.rstudio.com/src/contrib/GlobalOptions_0.0.12.tar.gz"
    list_url = homepage

    version('0.0.12', '6c268b3b27874918ba62eb0f6aa0a3e5')

    depends_on('r-testthat', type=('build', 'run'))
    depends_on('r-knitr', type=('build', 'run'))
    depends_on('r-markdown', type=('build', 'run'))
