using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour { 
  private CharacterController cController;

    private AudioSource FootStepsSound;
private float speed = 5;
private float angularSpeed = 100;
private float rotationAboutY = 0;
private float rotationAboutX = 0;
public GameObject aCamera; // must be connected in UNITY to camera
                           // Start is called before the first frame update
void Start()
{
    // connect CharacterController of Player to cController
    cController = GetComponent<CharacterController>();
        Cursor.lockState = CursorLockMode.Locked;
      //  Cursor.visible = false;
        FootStepsSound = GetComponent<AudioSource>();
    }

// Update is called once per frame
void Update()
{
    float dx, dz;

    // applies on camera
    rotationAboutX -= Input.GetAxis("Mouse Y") * angularSpeed * Time.deltaTime;
        if (!(rotationAboutX > 90.0f || rotationAboutX < -90.0f))
        {
            aCamera.transform.localEulerAngles = new Vector3(rotationAboutX, 0, 0);
        }

    // applies on player(and camera)
    rotationAboutY += Input.GetAxis("Mouse X") * angularSpeed * Time.deltaTime;
        
    transform.localEulerAngles = new Vector3(0, rotationAboutY, 0);
    // Input.GetAxis("Horizontal") can be: -1, 0 , 1
    dx = Input.GetAxis("Horizontal") * speed * Time.deltaTime;
    // Input.GetAxis("Vertical") can be: -1, 0 , 1
    dz = Input.GetAxis("Vertical") * speed * Time.deltaTime;
    // simple motion
    // this.transform.Translate(new Vector3(0, 0, 0.03f)); // changes z coordinate of THIS
    Vector3 motion = new Vector3(dx, -1, dz); // we consider dx and dz as LOCAL coordinates
    motion = transform.TransformDirection(motion); // changes motion from loca to global coordinates
                                                   // Move is based on GLOBAL coordinates
    cController.Move(motion);
        if (Mathf.Abs(motion.z) > 0.01f || Mathf.Abs(motion.x) > 0.01f)//only on player movement
        {
            if (!FootStepsSound.isPlaying)
            {
                FootStepsSound.Play();
            }
        }
}
}
