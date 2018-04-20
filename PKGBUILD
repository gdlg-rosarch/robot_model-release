# Script generated with Bloom
pkgdesc="ROS - The Kinematics and Dynamics Library (KDL) defines a tree structure to represent the kinematic and dynamic parameters of a robot mechanism. <tt>kdl_parser</tt> provides tools to construct a KDL tree from an XML robot representation in URDF."
url='http://ros.org/wiki/kdl_parser'

pkgname='ros-lunar-kdl-parser'
pkgver='1.12.9_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin>=0.5.68'
'ros-lunar-cmake-modules'
'ros-lunar-orocos-kdl>=1.3.0'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-urdf'
)

depends=('ros-lunar-orocos-kdl>=1.3.0'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-urdf'
)

conflicts=()
replaces=()

_dir=kdl_parser
source=()
md5sums=()

prepare() {
    cp -R $startdir/kdl_parser $srcdir/kdl_parser
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

