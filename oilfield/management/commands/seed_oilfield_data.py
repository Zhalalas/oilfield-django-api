from django.core.management.base import BaseCommand
from oilfield.models import OilField, Well, Sensor, ProductionReading
from django.utils import timezone
import random
class Command(BaseCommand):
    help = 'Seed the database with sample oil field data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        ProductionReading.objects.all().delete()
        Sensor.objects.all().delete()
        Well.objects.all().delete()
        OilField.objects.all().delete()

        # Create oil fields
        for i in range(1, 4):
            oil_field = OilField.objects.create(
                name=f'Oil Field {i}',
                location=f'Location {i}',
                operator_company=f'Operator {i}',
                start_date=timezone.now().date()
            )
            self.stdout.write(self.style.SUCCESS(f'Created {oil_field}'))

            # Create wells for each oil field
            for j in range(1, 4):
                well = Well.objects.create(
                    oil_field=oil_field,
                    name=f'Well {j} of {oil_field.name}',
                    status=random.choice(['active', 'shut-in', 'abandoned']),
                    drill_date=timezone.now().date(),
                    depth_m=random.uniform(1000, 5000)
                )
                self.stdout.write(self.style.SUCCESS(f'Created {well}'))

                # Create sensors for each well
                for k in range(1, 4):
                    sensor = Sensor.objects.create(
                        well=well,
                        sensor_type=random.choice(['pressure', 'temperature', 'flow_rate']),
                        install_date=timezone.now().date(),
                        is_active=random.choice([True, False])
                    )
                    self.stdout.write(self.style.SUCCESS(f'Created {sensor}'))

                    # Create production readings for each sensor
                    for l in range(1, 6):
                        reading = ProductionReading.objects.create(
                            sensor=sensor,
                            value=random.uniform(0, 100),
                            unit='units'
                        )
                        self.stdout.write(self.style.SUCCESS(f'Created {reading}'))