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

import os
import spack


class UrlListTest(Package):
    """Mock package with url_list."""
    homepage = "http://www.url-list-example.com"

    web_data_path = os.path.join(spack.test_path, 'data', 'web')
    url = 'file://' + web_data_path + '/foo-0.0.0.tar.gz'
    list_url = 'file://' + web_data_path + '/index.html'
    list_depth = 3

    version('0.0.0')
    version('1.0.0')
    version('3.0')
    version('4.5')
    version('2.0.0b2')
    version('3.0a1')
    version('4.5-rc5')

    def install(self, spec, prefix):
        pass
