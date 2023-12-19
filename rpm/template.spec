%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rmf-task-ros2
Version:        2.2.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmf_task_ros2 package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       json-devel
Requires:       ros-iron-nlohmann-json-schema-validator-vendor
Requires:       ros-iron-rclcpp
Requires:       ros-iron-rmf-api-msgs
Requires:       ros-iron-rmf-task-msgs
Requires:       ros-iron-rmf-traffic
Requires:       ros-iron-rmf-traffic-ros2
Requires:       ros-iron-rmf-utils
Requires:       ros-iron-rmf-websocket
Requires:       ros-iron-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  json-devel
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-nlohmann-json-schema-validator-vendor
BuildRequires:  ros-iron-rclcpp
BuildRequires:  ros-iron-rmf-api-msgs
BuildRequires:  ros-iron-rmf-task-msgs
BuildRequires:  ros-iron-rmf-traffic
BuildRequires:  ros-iron-rmf-traffic-ros2
BuildRequires:  ros-iron-rmf-utils
BuildRequires:  ros-iron-rmf-websocket
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-catch2
BuildRequires:  ros-iron-ament-cmake-uncrustify
%endif

%description
A package managing the dispatching of tasks in RMF system.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Tue Dec 19 2023 Yadunund <yadunund@openrobotics.org> - 2.2.4-1
- Autogenerated by Bloom

* Wed Sep 20 2023 Yadunund <yadunund@openrobotics.org> - 2.2.3-1
- Autogenerated by Bloom

* Mon Sep 11 2023 Yadunund <yadunund@openrobotics.org> - 2.2.2-1
- Autogenerated by Bloom

* Thu Aug 10 2023 Yadunund <yadunund@openrobotics.org> - 2.2.1-1
- Autogenerated by Bloom

* Wed Jun 07 2023 Yadunund <yadunund@openrobotics.org> - 2.2.0-1
- Autogenerated by Bloom

* Thu Apr 20 2023 youliang <youliang@openrobotics.org> - 2.1.2-3
- Autogenerated by Bloom

* Tue Mar 21 2023 youliang <youliang@openrobotics.org> - 2.1.2-2
- Autogenerated by Bloom

