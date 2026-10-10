# PlantShield — Django Plant Surveillance

**Academic Django project · grower and plant-health record management**

PlantShield provides Django views and models for farm accounts, trees, pests and disease information, and surveillance records. The source contains model relationships, registration and profile forms, authenticated management views, and templates for interacting with farm-specific records.

## Verified capabilities

- Django models for `Farm`, `Tree`, `PestDisease`, `PlantPart` and `SurveillanceRecord`
- Registration and user/farm profile workflows
- Surveillance records connected to farm, tree, pest/disease and severity
- Management and dashboard views; querysets restricted to the current farm context in the surveillance views
- SQLite development database included in the source tree

## Tech stack

Python, Django, SQLite, Django forms, class-based views and server-rendered templates.

## Repository map

```text
group-project-report-2/
  project_report/
    manage.py
    project_report/    # Django project settings, URLs and WSGI/ASGI
    pest_web/          # Models, forms, views, templates, migrations
    db.sqlite3         # Existing database tracked in repository
```

## Development setup (starting point)

1. Install Python and create a virtual environment.
2. Change directory to `group-project-report-2/project_report/`.
3. Install the Django version and other packages compatible with the source. **No reproducible requirements lockfile was verified**; do not assume a specific package version.
4. Set up a local development configuration with your own `SECRET_KEY`, `DEBUG` and permitted hosts. Do not deploy repository defaults to production.
5. Run `python manage.py migrate`, then `python manage.py runserver`.

The repository includes `db.sqlite3`; for a clean setup, use a separate blank development database after reviewing migrations and any fixture requirements. This setup has not been verified end to end.

## Implementation notes

The models capture relationships between growers and farms and between surveillance records, trees and pests. The views perform registration, update farm profiles and render per-farm management information. Follow the authentication checks and permission boundaries when adding features.

## Group project and attribution

This is a **university group project**. The repository confirms the architecture and features above, but individual ownership of each module should not be inferred from the presence of source code alone.

## Portfolio

[Read the project case study](https://sovanndevid.xyz/projects/plantshield.html)

## Security and privacy reminder

Before any deployment or open-source promotion, review `settings.py`, tracked SQLite data and commit history for secrets or personal information. Remove sensitive values and rotate exposed credentials if necessary. Do not publish production data or internal workplace material.
