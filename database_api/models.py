from django.db import models

# Create your models here.
#資料庫中創建字段

class Teacher(models.Model):
    T_id = models.AutoField(primary_key=True)
    T_Name = models.TextField(max_length=30)
    T_Email = models.TextField(max_length=50)
    T_Password = models.TextField(max_length=50)

    def __str__(self):
        return self

    class Meta:
        db_table = 'teacher'

class Student(models.Model):
    S_id = models.AutoField(primary_key=True)
    S_Name = models.TextField(max_length=30)
    S_Email = models.TextField(max_length=50)
    S_Password = models.TextField(max_length=50)

    def __str__(self):
        return self

    class Meta:
        db_table = 'student'

class Course(models.Model):
    C_id = models.AutoField(primary_key=True)
    T_id = models.ForeignKey(Teacher, on_delete=models.CASCADE,to_field="T_id")
    C_Name = models.TextField(max_length=30)

    def __str__(self):
        return self

    class Meta:
        db_table = 'course'

class Race_Answer(models.Model):
    R_id = models.AutoField(primary_key=True)
    C_id = models.ForeignKey(Course, on_delete=models.CASCADE, to_field="C_id")
    Race_doc = models.TextField(max_length=255)
    S_id = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="S_id")
    Status = models.BooleanField(default=True)
    C_Name = models.TextField(max_length=30)
    Time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self

    class Meta:
        db_table = 'race_answer'

class Race_List(models.Model):
    R_id = models.ForeignKey(Race_Answer, on_delete=models.CASCADE, to_field="R_id")
    S_id = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="S_id")
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'race_list'

class Sign(models.Model):
    Sign_id = models.AutoField(primary_key=True)
    C_id = models.ForeignKey(Course, on_delete=models.CASCADE, to_field="C_id")
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'sign'

class Sign_Record(models.Model):
    SR_id = models.AutoField(primary_key=True)
    Sign_id = models.ForeignKey(Sign, on_delete=models.CASCADE, to_field="Sign_id")
    S_id = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="S_id")
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'sign_record'

class Team_Desc(models.Model):
    TeamDesc_id  = models.AutoField(primary_key=True)
    Team_doc = models.TextField(max_length=255)
    Group_Total = models.DecimalField(max_digits=38, decimal_places=38)
    Group_limit = models.DecimalField(max_digits=38, decimal_places=38)
    C_id = models.ForeignKey(Course, on_delete=models.CASCADE, to_field="C_id")
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'team_desc'

class Team(models.Model):
    Team_id = models.AutoField(primary_key=True)
    Team_desc = models.ForeignKey(Team_Desc, on_delete=models.CASCADE, to_field="TeamDesc_id")
    Group_number = models.TextField(max_length=50)
    Leader_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self

    class Meta:
        db_table = 'team'

class Team_Member(models.Model):
    TeamMember_id = models.AutoField(primary_key=True)
    S_id = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="S_id")
    Team_id = models.ForeignKey(Team, on_delete=models.CASCADE, to_field="Team_id")
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        db_table = 'team_member'
