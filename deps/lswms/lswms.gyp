{
  'includes': [ '../common.gyp' ],
  'targets': [
    {
      'target_name': 'liblswms',
      'type': 'static_library',
      'dependencies': [
        '../opencv/opencv.gyp:libopencv'
      ],
      'include_dirs': [
        '../opencv/include',
        '../opencv/modules/core/include',
        '../opencv/modules/imgproc/include',
      ],
      'sources': [
        'LSWMS.cpp',
      ],
    },
  ]
}
