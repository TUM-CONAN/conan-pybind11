from conans import ConanFile, CMake, tools
import os


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.2.1"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/ulricheck/conan-pybind11"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

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
        cmake.configure(source_dir='source')
        cmake.build()
        cmake.install()

    def package_id(self):
        self.info.header_only()

    def package(self):
        pass
