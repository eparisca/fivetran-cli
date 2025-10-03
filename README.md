# Fivetran CLI 

A simple Fivetran API client for the command-line.

## Dependencies

* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* A Fivetran API Key and Secret

## Installation

### Linux / macOS

```bash
make install
```

## Run unit tests

```bash
make test
```

## `fivetran` menu

```bash
./fivetran --help
```

## Querying Fivetran API

```bash
export FIVETRAN_APIKEY="YOUR_API_KEY"
export FIVETRAN_APISECRET="YOUR_API_SECRET"
./fivetran destination list
```

Tip: Pipe the outputs to [jq](https://jqlang.org/download/) to filter results

Example:
```bash
./fivetran destination list | jq '.[] | select(.private_link_id != null) | {id, name, private_link_id}'
```

