import gi
from typing import Literal
from collections.abc import Iterable
from fabric.widgets.widget import EVENT_TYPE
from fabric.widgets.container import Container

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk


class EventBox(Gtk.Box, Container): # Changed Gtk.EventBox to Gtk.Box
    def __init__(
        self,
        events: EVENT_TYPE # This parameter will be handled differently or removed later
        | Gdk.EventMask
        | Iterable[EVENT_TYPE | Gdk.EventMask]
        | None = None,
        child: Gtk.Widget | None = None,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        h_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        v_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        h_expand: bool = False,
        v_expand: bool = False,
        size: Iterable[int] | int | None = None,
        **kwargs,
    ):
        Gtk.Box.__init__(self) # Changed Gtk.EventBox to Gtk.Box
        Container.__init__(
            self,
            # For Gtk.Box, the child is typically added after initialization
            # or via specific packing methods. We'll add it later if provided.
            None, # Child will be handled by Container logic or explicitly added
            name,
            name,
            visible,
            all_visible,
            style,
            style_classes,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            size,
            **kwargs,
        )
        # self.add_events(events) if events is not None else None # Removed add_events call
        # If a child is provided, add it to the Gtk.Box
        if child is not None:
            self.append(child) # Gtk.Box uses append (or pack_start, pack_end)

        # TODO: Process 'events' to add appropriate Gtk.EventControllers
        # For now, this functionality is deferred.
