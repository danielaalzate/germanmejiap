---
name: Germán Rodrigo Mejía Pavony
description: Warm editorial identity for a historian, researcher and speaker.
colors:
  primary: "#a43d18"
  primary-hover: "#7e2c10"
  paper: "#fff8ed"
  ink: "#262522"
  book-surface: "#f3eadb"
  muted: "#57564f"
  border: "#d9cfc0"
  link: "#97360f"
  invitation: "#973815"
  white: "#ffffff"
  focus: "#ba5429"
typography:
  display:
    fontFamily: "Editorial, Georgia, serif"
    fontSize: "clamp(48px, 5.6vw, 86px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-.035em"
  headline:
    fontFamily: "Editorial, Georgia, serif"
    fontSize: "clamp(38px, 4vw, 60px)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-.028em"
  title:
    fontFamily: "Editorial, Georgia, serif"
    fontSize: "30px"
    fontWeight: 400
    lineHeight: 1.05
  body:
    fontFamily: "Source, 'Segoe UI', sans-serif"
    fontSize: "18px"
    lineHeight: 1.55
  label:
    fontFamily: "Source, 'Segoe UI', sans-serif"
    fontSize: "12px"
    fontWeight: 600
    letterSpacing: ".23em"
spacing:
  compact: "16px"
  medium: "30px"
  section: "90px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    padding: "13px 23px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.white}"
    padding: "13px 23px"
  text-link:
    textColor: "{colors.link}"
    padding: "0"
  input:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    padding: "12px"
---

# Design System: Germán Rodrigo Mejía Pavony

## Overview

**Creative North Star: "A historian's editorial archive"**

Warm paper, literary typography and documentary photographs frame a living historian's work. Generous whitespace and restrained controls keep the reading experience clear.

**Key Characteristics:**
- Cream paper with burnt-orange accents.
- Garamond headlines and practical sans-serif reading text.
- Natural photographic proportions and asymmetrical book arrangements.

## Colors

Burnt orange marks primary actions, small rules and book arrows. Darker orange supplies hover feedback; the invitation band has its own warm orange. Paper and ink carry the main reading surfaces. A darker paper tone distinguishes books; neutral borders define press rows. White text sits over shaded photographs.

## Typography

The approved pairing is EB Garamond and Source Sans 3, locally registered as `Editorial` and `Source`. Keep headings regular and tightly set; use the sans serif for navigation, controls and metadata. Uppercase eyebrow labels include a short horizontal rule. Mobile hero text is 52px; section-specific mobile headline overrides remain in the stylesheet.

## Layout

The desktop container is at most 1240px wide, with 56px side margins. At 1000px and below, margins become 28px; at 720px and below, major columns stack and navigation becomes an expandable menu. Large-screen adjustments begin at 1700px.

Conference illustrations form a vertical list. Books use unequal columns, staggered top offsets and modest rotations; their positions do not align with conference topics. On mobile, two books share the first row and the third sits centered below. Press places its heading above a feature and two thumbnail rows.

Hero and desktop radio banners use proportional cover cropping. The portrait has a 1.7 frame with an additional inset crop; it is never stretched. Mobile radio switches to a naturally sized photograph below its text, with no overlay. Preserve these final stylesheet overrides.

## Elevation & Depth

Most surfaces stay flat. Warm book shadows suggest physical objects; a light edge treatment gives two covers thickness. Dialogs use a deep ambient shadow and blurred dark backdrop. Navigation has a subtle shadow when expanded on mobile. Exact shadow and motion values are recorded in the sidecar.

## Shapes

Controls and panels use straight edges and fine borders. Illustrations are monochrome and blended into paper; photographs retain their proportions even where a frame crops them.

## Components

Primary buttons have a fine accent border, a 48px minimum height and a small upward movement on hover. Outline buttons appear on dark photography and become white on hover. Text links use an offset underline. Interactive controls expose a 3px focus outline with a 5px offset.

The header pairs a Garamond wordmark with compact sans-serif navigation. Book controls lift and straighten on hover. Dialogs use the paper surface, scrolling within an 88vh maximum height. Inputs use white fills and muted warm borders. Reduced-motion preferences disable transitions and smooth scrolling.

Video media and the contact destination remain pending. Do not present a functioning video player or claim a message was sent until actual media or delivery integration exists.

## Do's and Don'ts

- Do preserve natural image proportions.
- Do retain the vertical conference list and asymmetrical book gallery.
- Do use the approved cream, burnt-orange and literary typography system.
- Don't add explanatory paragraphs beneath the conference or book headings.
- Don't imply that pending video or contact delivery works.
- Don't repeat the geographic exploration section.
