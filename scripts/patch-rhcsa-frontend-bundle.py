#!/usr/bin/env python3
"""Patch a compiled GIRUS frontend bundle to expose the RHCSA filter.

The GIRUS repository used for these labs does not include the frontend source
that produced the minified bundle served by the Nginx pod. This script applies
the same small runtime patch used in the local lab environment:

- add RHCSA as a sibling filter chip after CKA;
- filter `rhcsa-*` labs by RHCSA and Linux;
- keep numeric ordering for RHCSA labs;
- render RHCSA cards with the Red Hat icon.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def replace_once(source: str, old: str, new: str, label: str) -> str:
    if old not in source:
        if new in source:
            return source
        raise SystemExit(f"Pattern not found for {label}")
    return source.replace(old, new, 1)


def patch_bundle(source: str) -> str:
    cka_chip = (
        '(0,ls.jsx)(zl,{label:"CKA",onClick:()=>b("cka"),'
        'className:n.filterChip,color:"cka"===y?"primary":"default"})'
    )
    rhcsa_chip = (
        '(0,ls.jsx)(zl,{label:"RHCSA",onClick:()=>b("rhcsa"),'
        'className:n.filterChip,color:"rhcsa"===y?"primary":"default"})'
    )
    source = replace_once(source, cka_chip, f"{cka_chip},{rhcsa_chip}", "RHCSA filter chip")

    source = replace_once(
        source,
        '"cka"===y?e.name.startsWith("cka-"):"challenge"!==y||o',
        '"cka"===y?e.name.startsWith("cka-"):"rhcsa"===y?e.name.startsWith("rhcsa-"):"challenge"!==y||o',
        "RHCSA filter branch",
    )
    source = replace_once(
        source,
        '"linux"===y?!t&&!e.name.startsWith("cka-")&&!n&&!r&&!i&&!o:',
        '"linux"===y?e.name.startsWith("rhcsa-")||!t&&!e.name.startsWith("cka-")&&!n&&!r&&!i&&!o:',
        "Linux filter branch",
    )
    source = replace_once(
        source,
        'sort(((e,t)=>"cka"===y?e.name.localeCompare(t.name,void 0,{numeric:!0}):0))',
        'sort(((e,t)=>"cka"===y||"rhcsa"===y?e.name.localeCompare(t.name,void 0,{numeric:!0}):0))',
        "RHCSA numeric sort",
    )

    source = replace_once(
        source,
        "${o?n.kubernetesCard:a?n.dockerCard:h?n.challengeCard:n.linuxCard}",
        '${o?n.kubernetesCard:a?n.dockerCard:e.name.startsWith("rhcsa-")?n.linuxCard:h?n.challengeCard:n.linuxCard}',
        "RHCSA card style",
    )
    source = replace_once(
        source,
        "${x(e.name,e.description)?n.k8sIcon:w(e.name,e.description)?n.dockerIcon:h?n.challengeIcon:n.linuxIcon}",
        '${x(e.name,e.description)?n.k8sIcon:w(e.name,e.description)?n.dockerIcon:e.name.startsWith("rhcsa-")?n.linuxIcon:h?n.challengeIcon:n.linuxIcon}',
        "RHCSA icon class",
    )
    source = replace_once(
        source,
        '):h?(0,ls.jsx)(gs.A,{style:{width:"100%",height:"100%",color:"#FF5722"}}):(0,ls.jsx)("img",{src:Hl,alt:"Linux Logo",style:{width:"100%",height:"100%",objectFit:"contain"}})',
        '):e.name.startsWith("rhcsa-")?(0,ls.jsx)("img",{src:"assets/images/rhcsa-redhat-icon.webp",alt:"Red Hat RHCSA Logo",style:{width:"100%",height:"100%",objectFit:"contain"}}):h?(0,ls.jsx)(gs.A,{style:{width:"100%",height:"100%",color:"#FF5722"}}):(0,ls.jsx)("img",{src:Hl,alt:"Linux Logo",style:{width:"100%",height:"100%",objectFit:"contain"}})',
        "RHCSA Red Hat icon",
    )
    source = replace_once(
        source,
        '!x(e.name,e.description)&&!w(e.name,e.description)&&!h&&(0,ls.jsx)(zl,{label:"Linux",className:`${n.chip} ${n.linuxChip}`})',
        '(e.name.startsWith("rhcsa-")||!x(e.name,e.description)&&!w(e.name,e.description)&&!h)&&(0,ls.jsx)(zl,{label:"Linux",className:`${n.chip} ${n.linuxChip}`})',
        "RHCSA Linux chip",
    )
    source = replace_once(
        source,
        "${x(e.name,e.description)?n.startButtonK8s:w(e.name,e.description)?n.startButtonDocker:h?n.startButtonChallenge:n.startButtonLinux}",
        '${x(e.name,e.description)?n.startButtonK8s:w(e.name,e.description)?n.startButtonDocker:e.name.startsWith("rhcsa-")?n.startButtonLinux:h?n.startButtonChallenge:n.startButtonLinux}',
        "RHCSA start button style",
    )

    if 'label:"RHCSA"' not in source:
        raise SystemExit("RHCSA label was not added")
    if 'label:"CKA"' not in source or source.index('label:"CKA"') > source.index('label:"RHCSA"'):
        raise SystemExit("RHCSA chip was not inserted after CKA")
    if "rhcsa-redhat-icon.webp" not in source:
        raise SystemExit("RHCSA icon reference was not added")

    return source


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch a compiled GIRUS frontend JS bundle for RHCSA.")
    parser.add_argument("input", type=Path, help="Original compiled main.*.js bundle")
    parser.add_argument("output", type=Path, help="Patched output bundle")
    args = parser.parse_args()

    source = args.input.read_text(encoding="utf-8")
    patched = patch_bundle(source)
    args.output.write_text(patched, encoding="utf-8")
    print(f"Patched RHCSA frontend bundle: {args.output}")


if __name__ == "__main__":
    main()
