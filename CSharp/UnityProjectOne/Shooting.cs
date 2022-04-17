using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shooting : MonoBehaviour
{
    public GameObject Enemy;
    public GameObject Camera;
    private Animator animator;
    private KnightMotion knightMotion;
    public ParticleSystem Flash;
    public GameObject Target;
    public GameObject Gun;
    public GameObject Muzzle;
    public AudioSource Gunshot;
    private LineRenderer BulletLine;


    // Start is called before the first frame update
    void Start()
    {
        knightMotion = GetComponent<KnightMotion>();
        Gunshot = GetComponent<AudioSource>();
        BulletLine = Gun.GetComponent<LineRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        RaycastHit hit;
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Flash.Play();
            Gunshot.PlayDelayed(0.8F);
            if (Physics.Raycast(Camera.transform.position, Camera.transform.forward, out hit))
            {
                //target is moved to the bullet hit
                Target.transform.position = hit.point;
                //drawBullet
                StartCoroutine(DrawShootingLine());

                Target.SetActive(true);
                
                if (hit.transform.gameObject == Enemy.transform.gameObject)
                {

                    StartCoroutine(HitAndGetUp());
                }
            }
        }
    }
      public IEnumerator HitAndGetUp()
    {

        animator.SetInteger("State", 2);
       yield return new WaitForSeconds(2);
        animator.SetInteger("State", 3);
        yield return new WaitForSeconds(2);
        animator.SetInteger("State", 4);
        yield return new WaitForSeconds(2);
        animator.SetInteger("State", 0);
    } 
    public IEnumerator DrawShootingLine()
    {
        BulletLine.SetPosition(0, Muzzle.transform.position);
        BulletLine.SetPosition(1, Target.transform.position);
        BulletLine.enabled = true;
        yield return new WaitForSeconds(0.01f);
        BulletLine.enabled = false; ;

      

    }
}
