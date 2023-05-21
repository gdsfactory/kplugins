import kfactory as kf
from kplugins.gmeep.write_sparameters_meep import write_sparameters_meep


def test_materials_override() -> None:
    """Checks that materials are properly overridden if index is provided."""

    c = kf.cells.waveguide(length=2, width=0.5, layer=0)

    # Default (materials strings)
    sp1 = write_sparameters_meep(
        c,
        run=False,
        animate=False,
        is_3d=False,
        overwrite=True,
    )

    # Override
    sp2 = write_sparameters_meep(
        c,
        run=False,
        animate=False,
        material_name_to_meep=dict(si=2.0),
        is_3d=False,
        overwrite=True,
    )

    assert sp1.geometry[0].material.epsilon(freq=1)[0][0] != 4.0
    assert sp2.geometry[0].material.epsilon(freq=1)[0][0] == 4.0


if __name__ == "__main__":
    test_materials_override()
