# encoding: utf-8
#
# Copyright (C) 2015 ycmd contributors
#
# This file is part of ycmd.
#
# ycmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ycmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ycmd.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
# Not installing aliases from python-future; it's unreliable and slow.
from builtins import *  # noqa

#  from hamcrest import assert_that, contains_string, has_item, has_items

from nose.tools import eq_
from ycmd import user_options_store
from ycmd.tests.test_utils import BuildRequest
from ycmd.request_wrap import RequestWrap
from ycmd.completers.tex.bib_completer import BibCompleter


def _ShouldUseNowForLine( completer,
                          contents,
                          extra_data = None,
                          column_num = None ):

  # Strictly, column numbers are *byte* offsets, not character offsets. If
  # the contents of the file contain unicode characters, then we should manually
  # supply the correct byte offset.
  column_num = len( contents ) + 1 if not column_num else column_num

  request = BuildRequest( column_num = column_num,
                          contents = contents )
  if extra_data:
    request.update( extra_data )

  request_data = RequestWrap( request )
  return completer.ShouldUseNow( request_data )


class BibCompleter_test( object ):
  def setUp( self ):
    self._bib_completer = BibCompleter(
      user_options_store.DefaultOptions() )


  def _ShouldUseNowForLine( self, contents, column_num=None ):
    return _ShouldUseNowForLine( self._bib_completer,
                                 contents,
                                 column_num = column_num )


  def ShouldUserNowForLine_test( self ):
    eq_( True, self._ShouldUseNowForLine( contents = "\\cite{" ) )
    eq_( False, self._ShouldUseNowForLine( contents = "\\textrm{" ) )
