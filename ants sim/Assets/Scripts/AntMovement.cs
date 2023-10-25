using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AntMovement : MonoBehaviour
{

    public float speed = 3f;
    public float rotationSpeed = 200.0f;
    private Vector3 target;

    // Start is called before the first frame update:
    void Start()
    {
        // Current Ant position:
        target = transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        // If left click:
        if (Input.GetMouseButtonDown(0))
        {
            // Converting click into coordinates:
            target = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            target.z = transform.position.z;

            // Calculating angle to rotate:
            Vector3 direction = target - transform.position;
            float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;

            // Rotating towards the mouse click:
            Quaternion rotation = Quaternion.AngleAxis(angle - 90.Vector3.forward);
            transform.rotation = Quaternion.Slerp(transform.rotation, rotation, rotationSpeed * Time.deltaTime);
        }

        // Move ant towards target:
        transform.position = Vector3.MoveTowards(transform.position, target, speed * Time.deltaTime);
    }
}
