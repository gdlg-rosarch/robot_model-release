# Script generated with Bloom
pkgdesc="ROS - This package contains a C++ parser for the Unified Robot Description Format (URDF), which is an XML format for representing a robot model. The code API of the parser has been through our review process and will remain backwards compatible in future releases."
url='http://ros.org/wiki/urdf'

pkgname='ros-kinetic-urdf'
pkgver='1.12.11_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.68'
'ros-kinetic-cmake-modules'
'ros-kinetic-pluginlib'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-urdf-parser-plugin'
'urdfdom'
'urdfdom-headers'
)

depends=('ros-kinetic-pluginlib'
'ros-kinetic-rosconsole-bridge'
'ros-kinetic-roscpp'
'ros-kinetic-urdf-parser-plugin'
'urdfdom'
'urdfdom-headers'
)

conflicts=()
replaces=()

_dir=urdf
source=()
md5sums=()

prepare() {
    cp -R $startdir/urdf $srcdir/urdf
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

