using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;


public class KnightMotion : MonoBehaviour
{
    private Animator animator;
    public GameObject Player;
    private NavMeshAgent agent;
    // Start is called before the first frame update
    void Start()
    {

        animator = GetComponent<Animator>();
        agent = GetComponent<NavMeshAgent>();
    }

    // Update is called once per frame
    void Update()
    {
        animator.SetInteger("State", 5);
        if (agent.enabled)
        {
            agent.SetDestination(Player.transform.position);
        }
        /*if (Input.GetKeyDown(KeyCode.Z))
        {
            animator.SetInteger("State", 1);
        }
        if (Input.GetKeyDown(KeyCode.X))
        {
            animator.SetInteger("State", 0);
        }
        if (Input.GetKeyDown(KeyCode.C))
        {
            StartCoroutine(HitAndGetUp());
       
        }*/

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
}
