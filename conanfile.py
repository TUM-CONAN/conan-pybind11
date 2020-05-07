from conans import ConanFile, CMake, tools
import os


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.5.0"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/ulricheck/conan-pybind11"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    options = {
        "with_system_python": [True, False],
    }

    default_options = {
        "with_system_python": True
    }

    def requirements(self):
        if self.options.with_system_python:
            self.requires("python_dev_config/[>=0.5]@camposs/stable")
        else:
            self.requires("python/3.8.2@camposs/stable")
            self.requires("python-setuptools/41.2.0@camposs/stable")
            self.requires("python-pip/[>=19.2.3]@camposs/stable")
            self.requires("cython/0.29.16@camposs/stable")
            self.requires("python-numpy/1.18.4@camposs/stable")

    def source(self):
        tools.download("https://github.com/pybind/pybind11/archive/v%s.tar.gz" % self.version,
                       "pybind11.tar.gz")
        tools.unzip("pybind11.tar.gz")
        os.rename("pybind11-%s" % self.version, "source")
        os.unlink("pybind11.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.definitions["PYBIND11_INSTALL"] = True
        cmake.configure(source_dir='source')
        cmake.build()
        cmake.install()

    def package_id(self):
        self.info.header_only()

    def package(self):
        pass
