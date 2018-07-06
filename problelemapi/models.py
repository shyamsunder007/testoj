from django.db import models
'''
$fields = array(
				'assignment'        => array('type' => 'SMALLINT', 'constraint' => 4, 'unsigned' => TRUE),
				'id'                => array('type' => 'SMALLINT', 'constraint' => 4, 'unsigned' => TRUE),
				'name'              => array('type' => 'VARCHAR', 'constraint' => 50, 'default' => ''),
				'score'             => array('type' => 'INT', 'constraint' => 11),
				'is_upload_only'    => array('type' => 'TINYINT', 'constraint' => 1, 'default' => '0'),
				'c_time_limit'      => array('type' => 'INT', 'constraint' => 11, 'unsigned' => TRUE, 'default' => 500),
				'python_time_limit' => array('type' => 'INT', 'constraint' => 11, 'unsigned' => TRUE, 'default' => 1500),
				'java_time_limit'   => array('type' => 'INT', 'constraint' => 11, 'unsigned' => TRUE, 'default' => 2000),
				'memory_limit'      => array('type' => 'INT', 'constraint' => 11, 'unsigned' => TRUE, 'default' => 50000),
				'allowed_languages' => array('type' => 'TEXT', 'default' => ''),
				'diff_cmd'          => array('type' => 'VARCHAR', 'constraint' => 20, 'default' => 'diff'),
				'diff_arg'          => array('type' => 'VARCHAR', 'constraint' => 20, 'default' => '-bB'),
			);'''
# Create your models here.
class Problems(models.Model):
    assignment=models.PositiveSmallIntegerField(max_length=20)
    Pid=models.PositiveSmallIntegerField(max_length=20)
    name=models.CharField(max_length=50,default='')
    score=models.IntegerField(max_length=11)
    is_upload_only=models.SmallIntegerField(max_length=1,default=0)
    c_time_limit=models.PositiveIntegerField(max_length=11,default=500)
    python_time_limit=models.PositiveIntegerField(max_length=11,default=1500)
    java_time_limit=models.PositiveIntegerField(max_length=11,default=2000)
    memory_limit=models.PositiveIntegerField(max_length=11,default=50000)
    allowed_languages=models.TextField(default='')
    diff_cmd=models.CharField(max_length=20,default='diff')
    diff_arg=models.CharField(max_length=20,default='-bB')
    
    
    def __str__(self):
        return self.name