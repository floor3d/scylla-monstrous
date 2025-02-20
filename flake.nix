{
  description = "A flake to benchmark and explore the monstrous ScyllaDB";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs =
    inputs@{
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShell = pkgs.mkShell {
          name = "python";
          buildInputs = with pkgs; [
            python3
            python3Packages.pip
            python3Packages.cassandra-driver
            cassandra
          ];
          shellHook = ''
            mkdir -p .venv
            export PIP_PREFIX=$(pwd)/.venv/pip_packages
            export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"
            export PATH="$PIP_PREFIX/bin:$PATH"
            unset SOURCE_DATE_EPOCH
          '';
          PYTHONBREAKPOINT = "ipdb.set_trace";
        };

        formatter = pkgs.nixfmt-rfc-style;
      }
    );
}
