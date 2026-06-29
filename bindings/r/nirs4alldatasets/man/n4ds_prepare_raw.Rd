\name{n4ds_prepare_raw}
\alias{n4ds_prepare_raw}
\title{Prepare Retrieved Raw Resources}
\usage{
n4ds_prepare_raw(request_json, opts_json = "")
}
\arguments{
\item{request_json}{A retrieval request as JSON: \code{{dataset_id, route}}.}
\item{opts_json}{Options as JSON: \code{{cache_dir?}}; \code{""} for defaults.}
}
\value{
The preparation status as a JSON string: \code{{dir, ok, route_id, resources}}.
}
\description{
Prepare already-retrieved raw resources with the Rust nirs4all reader stack.
}
