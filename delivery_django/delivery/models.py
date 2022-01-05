from django.db import models


class Customer(models.Model):
    # Field name made lowercase.
    cno = models.AutoField(db_column='cNo', primary_key=True)
    # Field name made lowercase.
    cname = models.CharField(db_column='cName', max_length=20)
    # Field name made lowercase.
    caddress = models.CharField(db_column='cAddress', max_length=50)
    phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.cname


class Deliveryman(models.Model):
    # Field name made lowercase.
    dno = models.AutoField(db_column='dNo', primary_key=True)
    # Field name made lowercase.
    dname = models.CharField(db_column='dName', max_length=20)
    phone = models.CharField(max_length=10)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'deliveryman'

    def __str__(self):
        return self.dname


class Food(models.Model):
    # Field name made lowercase.
    fno = models.AutoField(db_column='fNo', primary_key=True)
    # Field name made lowercase.
    rno = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='rNo')
    # Field name made lowercase.
    fname = models.CharField(db_column='fName', max_length=20)
    price = models.CharField(max_length=5)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'food'

    def __str__(self):
        return self.fname


class Orderform(models.Model):
    # Field name made lowercase.
    ono = models.AutoField(db_column='oNo', primary_key=True)
    # Field name made lowercase.
    dno = models.ForeignKey(Deliveryman, models.DO_NOTHING, db_column='dNo')
    # Field name made lowercase.
    cno = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cNo')
    # Field name made lowercase.
    fno = models.ForeignKey(Food, models.DO_NOTHING, db_column='fNo')
    content = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime')

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'orderform'

    def __str__(self):
        return str(self.ono)


class Restaurant(models.Model):
    # Field name made lowercase.
    rno = models.AutoField(db_column='rNo', primary_key=True)
    # Field name made lowercase.
    rname = models.CharField(db_column='rName', max_length=20)
    # Field name made lowercase.
    raddress = models.CharField(db_column='rAddress', max_length=50)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'restaurant'

    def __str__(self):
        return self.rname
