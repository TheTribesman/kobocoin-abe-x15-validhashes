# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .X15Chain import X15Chain

class Kobocoin(X15Chain, PpcPosChain):
    def __init__(chain, **kwargs):
        chain.name = 'Kobocoin'
        chain.code3 = 'KOB'
        chain.address_version = '\x23'
        chain.magic = '\xa1\xa0\xa2\xa3'
		chain.decimals = 8
        X15Chain.__init__(chain, **kwargs)
		
	def has_feature(chain, feature):
        return feature == 'nvc_proof_of_stake'

    datadir_conf_file_name = 'Kobocoin.conf'
    datadir_rpcport = 3341
    datadir_p2pport = 9011
