# Copyright 2015 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'default_run',
          'type': 'none',
          'dependencies': [
            '../gypfiles/cctest.gyp:cctest_run',
            'debugger/debugger.gyp:debugger_run',
            'fuzzer/fuzzer.gyp:fuzzer_run',
            'inspector/inspector.gyp:inspector-test_run',
            'intl/intl.gyp:intl_run',
            'message/message.gyp:message_run',
            'mjsunit/mjsunit.gyp:mjsunit_run',
            'preparser/preparser.gyp:preparser_run',
            'unittests/unittests.gyp:unittests_run',
            'wasm-spec-tests/wasm-spec-tests.gyp:wasm_spec_tests_run',
          ],
          'includes': [
            '../gypfiles/features.gypi',
            '../gypfiles/isolate.gypi',
          ],
          'sources': [
            'default.isolate',
          ],
        },
      ],
    }],
  ],
}
