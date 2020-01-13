# conan-pybind11

[Conan.io](https://conan.io) package for pybind11 library. 

## Build packages

    $ conan create . camposs/stable
    
## Upload packages to server

    $ conan upload pybind11/2.4.3@ulricheck/stable --all -r camp
    
## Reuse the packages

### Basic setup

    $ conan install pybind11/2.4.3@ulricheck/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    pybind11/2.4.3@ulricheck/stable
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
