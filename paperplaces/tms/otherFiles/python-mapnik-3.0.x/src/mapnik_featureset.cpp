/*****************************************************************************
 *
 * This file is part of Mapnik (c++ mapping toolkit)
 *
 * Copyright (C) 2015 Artem Pavlenko, Jean-Francois Doyon
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 *
 *****************************************************************************/

#include <mapnik/config.hpp>
#include "boost_std_shared_shim.hpp"

#pragma GCC diagnostic push
#include <mapnik/warning_ignore.hpp>
#include <boost/python.hpp>
#include <boost/noncopyable.hpp>
#pragma GCC diagnostic pop

// mapnik
#include <mapnik/feature.hpp>
#include <mapnik/datasource.hpp>

namespace {
using namespace boost::python;

inline object pass_through(object const& o) { return o; }

inline mapnik::feature_ptr next(mapnik::featureset_ptr const& itr)
{
    mapnik::feature_ptr f = itr->next();
    if (!f)
    {
        PyErr_SetString(PyExc_StopIteration, "No more features.");
        boost::python::throw_error_already_set();
    }

    return f;
}

}

void export_featureset()
{
    using namespace boost::python;
    // Featureset implements Python iterator interface
    class_<mapnik::Featureset, std::shared_ptr<mapnik::Featureset>,
           boost::noncopyable>("Featureset", no_init)
        .def("__iter__", pass_through)
        .def("__next__", next)
        // Python2 support
        .def("next", next)
        ;
}
