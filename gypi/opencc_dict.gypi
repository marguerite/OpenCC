{
  "targets": [{
    "target_name": "opencc_dict",
    "type": "executable",
    "sources": [
      "../src/DartsDict.cpp",
      "../src/Dict.cpp",
      "../src/DictConverter.cpp",
      "../src/DictGroup.cpp",
      "../src/TextDict.cpp",
      "../src/UTF8Util.cpp",
    ],
    "include_dirs": [
      "../src",
      "../deps/darts-clone"
    ]
  }]
}
