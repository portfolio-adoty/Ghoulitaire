extends Camera2D

onready var player = get_parent().get_node("Player")
onready var area = get_node("Area2D")
onready var tween = get_node("Tween")

var width = 160
var height = 144

var inputs = {
	"right" : Vector2.RIGHT,
	"left" : Vector2.LEFT,
	"up" : Vector2.UP,
	"down" : Vector2.DOWN
}

func _process(delta):
	
	if tween.is_active():
		
		return
	
	if !player in area.get_overlapping_areas():
		
		if player.position.x > position.x + width / 2:
			
			move(inputs["right"], width)
		
		if player.position.x < position.x - width / 2:
			
			move(inputs["left"], width)
		
		if player.position.y > position.y + height / 2:
			
			move(inputs["down"], height)
		
		if player.position.y < position.y - height / 2:
			
			move(inputs["up"], height)

func move(direction, screen_direction):
	
	#position += direction * screen_direction
	tween.interpolate_property(self, "position",
		position, position + (direction * screen_direction),
		1.0 / 8, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
	
	tween.start()
	#yield(tween, "tween_completed")
